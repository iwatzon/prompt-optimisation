from dotenv import load_dotenv
import os
from algorithms.utils import get_json
from langchain.chat_models import ChatOpenAI
from langchain_community.llms import HuggingFaceEndpoint
import json
import asyncio

load_dotenv()


class ReviewPrincipals:
    def __init__(self, core_principles: list):
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


class ReviewAgent:
    """
    This class represents a voting agent that reviews a selection of prompts and votes for the best based on its persona and core principles.
    """
    def __init__(self, persona_title: str, core_principles: ReviewPrincipals, model: str='gpt-4o', temperature: float=1.0):
        """
        Initializes the PromptReviewAgent with a persona title, core principles, model, and temperature.
        
        :param persona_title: The title of the persona for the agent.
        :param core_principles: The core principles of the agent.
        :param model: The model to be used by the agent. Default is 'gpt-4o'.
        :param temperature: The temperature to be used by the agent. Default is 1.0.
        """
        self.persona_title = persona_title
        self.core_principles = str(core_principles)
        self.llm = ChatOpenAI(temperature=temperature, model=model)
    
    async def review(self, prompts_to_review: dict):
        """
        Reviews multiple sets of prompts and returns the best from each set.
        
        :param prompts_to_review: The prompts to be reviewed.
        :return: A results dict.
        """
        instruction = f"""You are a senior {self.persona_title}. 
        You have been asked to review the following mutated prompts: {prompts_to_review}.
        You should consider the prompts in light of your core principles, providing positive and negative feedback for each prompt.
        You should also score the prompts based on how well they align with your core principles. The score should be an integer between 0 and 100.
        
        Your core principles are:
        {self.core_principles}

        The output must be json code with the following format:
        {{
            "mutation prompt 1": {{
                    "orignal prompt": "orignal prompt",
                    "mutated prompt": "mutated prompt",
                    "positives": "positives of the prompt",
                    "negatives": "negatives of the prompt",
                    "score": "score of the prompt",
                }},
                ...
        }}
        """

        model_output = await self.llm.ainvoke(instruction)
        json_output = get_json(model_output)

        if json_output is None:
            json_output = model_output.content

        return json.loads(json_output)
    

class SwarmEvaluation():
    """
    Use swarm intelligence to perfrom evaluation using majority voting to select top mutated prompt for each offspring.
    Each agent in the swarm is an expert on a single aspect of the requirements for the prompt.
    """
    
    def __init__(self, prompts: dict):
        """
        Initializes the SwarmEvaluation
        """
        self.prompts = prompts
        self.reviewers = {}
        self.review_results = {}

    def register_reviewer(self, reviewer: ReviewAgent):
        """
        Register a voter for the majority vote process.
        """
        self.reviewers[reviewer.persona_title] = reviewer

    async def review(self):
        """
        Executes the voting process by calling each voter to vote on the prompt in parallel. 
        Concatenates the votes and returns the result as a dict with the voter persona titles as the keys.
        """
        tasks = []
        for persona_title, reviewer in self.reviewers.items():
            task = asyncio.create_task(reviewer.review(self.prompts))
            tasks.append(task)
        
        results = await asyncio.gather(*tasks)
        
        for i, persona_title in enumerate(self.reviewers.keys()):
            self.review_results[persona_title] = results[i]
        
        return self.review_results 
    

class PromptSelectionAgent:

    def __init__(self, prompts: dict):
        self.prompts = prompts

    def select(self):

        # Load openai language model
        llm = ChatOpenAI(
            temperature=0.5,
            model='gpt-4o'
        )

        # Agent instruction
        instruction = f"""
        You are an expert prompt engineer. Select the best prompt from the following list of prompts: {self.prompts}.
        Consider the task at hand and the end user (an LLM) of the prompt.
        Justify why you think the selected prompt is the best choice.

        The output must be json code containing the selected prompt with the following format:
        {{
            "selected prompt": "prompt content",
            "justification": "justification"
        }}
        """

        # Generate new generation of prompts
        model_output = llm.invoke(instruction)
        json_output = get_json(model_output)

        if json_output is None:
            json_output = model_output.content

        return json.loads(json_output)