# reviewer swarm class

from uuid import uuid4
import dotenv
from pydantic import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from typing import List
import json

dotenv.load_dotenv()

# class SuggestedUpdate(BaseModel):
#     original: str = Field(..., description="The original value of the section of the prompt should be updated")
#     updated: str = Field(..., description="The updated value of the section of the prompt should be updated")
    

class ApprovalResponse(BaseModel):
    original_prompt: str = Field(..., description="The original prompt that was reviewed")
    approved: bool = Field(..., description="Whether the request was approved or not, True or False")
    explanation: str = Field(..., description="A detailed explanation of why the request was approved or not")
    # partial_updates: List[SuggestedUpdate] = Field(..., description="The sections of the prompt need to be updated, and the new values")

class PromptReviewPrincipals:
    def __init__(self, core_principles: List[str]):
        self.core_principles = core_principles
    
    def add_principle(self, principle: str):
        """
        Adds a principle to the core principles list.
        
        :param principle: The principle to be added.
        """
        self.core_principles.append(principle)
        
    def __str__(self):
        """
        Returns a string representation of the core principles, each principle is listed on a new line with a preceding dash.
        
        Example:
        - principle 1
        - principle 2
        ...
        """
        return "\n".join([f"- {principle}" for principle in self.core_principles])
    

class PromptReviewAgent:
    """
    This class represents an approval agent that reviews and approves requests based on its persona and core principles.
    """
    def __init__(self, persona_title: str, core_principles: PromptReviewPrincipals, model:str='gpt-4o', temperature: float=1.0):
        """
        Initializes the PromptReviewAgent with a persona title, core principles, model, and temperature.
        
        :param persona_title: The title of the persona for the agent.
        :param core_principles: The core principles of the agent.
        :param model: The model to be used by the agent. Default is 'gpt-4o'.
        :param temperature: The temperature to be used by the agent. Default is 0.0.
        """
        self.id = uuid4()
        self.persona_title = persona_title
        self.core_principles = str(core_principles)
        self.llm = ChatOpenAI(temperature=temperature,model=model)
    
    async def review(self, prompt_to_review: str) -> ApprovalResponse:
        """
        Reviews a given prompt and returns an ApprovalResponse.
        
        :param prompt_to_review: The prompt to be reviewed.
        :return: An ApprovalResponse object containing the review results.
        """
        prompt_template = """You are a senior {persona_title}. You have been asked to review the following request and provide your approval or disapproval. 
        You should consider the request in light of your core principles and provide a detailed explanation on why you approve or disapprove of the request.
        Be constructive in your feedback and provide suggestions on how the request could be improved.
        
        **Your core principles are:**
        {core_principles}
        
        **Strict guidelines:**
        1. All restrictions already stated in the text being reviewed should not be modified.
        2. All negations should be preserved. e.g. "DO NOT" should not be changed to "DO" or removed entirely.
        3. All placeholders denoted by curly braces should not be modified or removed.
        4. Adding additional restrictions or negations is allowed.
        5. Adding additional placeholders is not allowed.
        6. Adding additional instructions to achieve your core principles is allowed.
        
        **Request to review:**
        -------------------------------------
        {prompt_to_review}
        -------------------------------------
        
        {format_instructions}
        """
        pydantic_parser = PydanticOutputParser(pydantic_object=ApprovalResponse)
        format_instructions = pydantic_parser.get_format_instructions()

        prompt = ChatPromptTemplate.from_template(prompt_template)
        messages = prompt.format_messages(persona_title=self.persona_title, prompt_to_review=prompt_to_review,core_principles=self.core_principles, format_instructions=format_instructions)

        for _ in range(3):
            try:
                output = self.llm(messages=messages)
                approval_summary = pydantic_parser.parse(output.content)
                break
            except Exception:
                continue
        else:
            raise Exception("Failed to parse output after 3 attempts")
        return approval_summary


class PromptAgent:
    """
    This class represents a prompt agent that manages the base prompt and updates it based on suggested updates.
    """
    def __init__(self, base_prompt: str):
        """
        Initializes the PromptAgent with a base prompt.
        
        :param base_prompt: The base prompt to be managed by the agent.
        """
        self.base_prompt = base_prompt
        self.llm = ChatOpenAI(model='gpt-4o', temperature=0.5)

        
    # async def update(self, suggested_update: SuggestedUpdate)->str:
    #     """
    #     Updates the base prompt based on a given SuggestedUpdate and returns the updated prompt.
        
    #     :param suggested_update: The SuggestedUpdate to be applied to the base prompt.
    #     :return: The updated base prompt.
    #     """
    #     for update in suggested_update:
    #         self.base_prompt = self.base_prompt.replace(update.original, update.updated)
            
    #     return self.base_prompt

    async def update(self, orgiginal_prompt: str, explanation: str)->str:
        """
        Updates the base prompt based on explanantion given in the ApprovalResponse and generates an improved prompt.
        """

        prompt_template = """You are an expert prompt engineer. You have been tasked with updating the following prompt based on the feedback provided by a reviewer.
        You should consider the feedback provided and update the prompt accordingly.

        **Original Prompt:**
        {original_prompt}

        **Feedback:**
        {explanation}

        Output the updated prompt.
        """
        prompt = ChatPromptTemplate.from_template(prompt_template)
        messages = prompt.format_messages(original_prompt=orgiginal_prompt, explanation=explanation)

        try:
            output = self.llm(messages=messages)
            self.base_prompt = output.content
        except:
            return self.base_prompt
                
        return self.base_prompt
        

class SequentialPromptReview:
    """
    This class represents a sequential approval process. It registers agents and manages the approval process.
    """
    def __init__(self, prompt_agent: PromptAgent, max_resets: int = 10):
        """
        Initializes the SequentialPromptReview with a prompt agent and a maximum number of resets.
        
        :param prompt_agent: The agent that provides the prompt for the approval process.
        :param max_resets: The maximum number attempts to reach approval consensus.
        """
        self.approvers = []
        self.prompt = prompt_agent.base_prompt
        self.base_prompt = prompt_agent.base_prompt
        self.prompt_agent = prompt_agent
        self.approved = {}
        self.max_resets = max_resets

    def register_approver(self, approver: PromptReviewAgent):
        """
        Registers an approver for the sequential approval process.
        
        :param approver: The approver to be registered.
        """
        self.approvers.append(approver)

    def reset_approval(self):
        """
        Resets the approval process by clearing the approved dictionary.
        """
        self.approved = {}

    async def review(self) -> str:
        """
        Executes the approval process. It iterates over the registered approvers and asks them to review the prompt.
        If an approver does not approve, the prompt is updated and the approval process is reset.
        The process continues until all approvers have approved or the maximum number of resets has been reached.
        
        :return: The final approved prompt.
        """
        reset_count = 0
        while len(self.approved) < len(self.approvers) and reset_count < self.max_resets:
            for approver in self.approvers:
                if approver.id not in self.approved:
                    result = await approver.review(self.prompt)
                    if result.approved:
                        self.approved[approver.id] = result
                    else:
                        self.prompt = await self.prompt_agent.update(result.original_prompt, result.explanation)
                        self.reset_approval()
                        reset_count += 1
                        break
                    
        if reset_count >= self.max_resets:
            return self.base_prompt
        
        return self.prompt