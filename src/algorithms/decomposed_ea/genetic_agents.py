from dotenv import load_dotenv
import os
from algorithms.utils import get_json
from langchain.chat_models import ChatOpenAI
from langchain_community.llms import HuggingFaceEndpoint
import json

load_dotenv()

class ThinkingStylesAgent:

    def __init__(self, n: int, base_prompt: str):
        self.n = n
        self.base_prompt = base_prompt

    def generate(self):
        """
        Agent that generates n different prompts with different thinking styles to approach a probelm.
        """

        # Load open source language model
        # model = "mistralai/Mistral-7B-Instruct-v0.3"
        # llm = HuggingFaceEndpoint(
        #     repo_id=model,
        #     huggingfacehub_api_token=hf_api_token
        # )

        # Load openai language model
        llm = ChatOpenAI(
            temperature=0.5,
            model='gpt-4o'
        )

        # Agent instruction
        instruction = f"""
        You are an expert thinker and problem solver. Here is a base prompt: {self.base_prompt}
        Generate {self.n} prompts to elaborate on the base prompt, each with a unique thinking style. 
        Consider the context of the problem and the end user (an LLM) of the prompt.
        
        The output should be json code containing {self.n} prompts with the following format:
        {{
            "style 1": {{
                "prompt": "prompt content",
                "thinking style": "thinking style",
            }},
            "style 2": {{
                "prompt": "prompt content",
                "thinking style": "thinking style",
            }},
            ...
        }}
        """

        # Generate prompts
        model_output = llm.invoke(instruction)
        json_output = get_json(model_output)

        if json_output is None:
            json_output = model_output.content

        return json.loads(json_output)


class BreederAgent:
    """
    Agent that pairs two prompts and breeds them to create new a prompt.
    """

    def __init__(self, prompts: dict, n: int):
        self.prompts = prompts
        self.n = n

    def generate(self):
        """
        Generate pairs of prompts.
        """

        # Load openai language model
        llm = ChatOpenAI(
            temperature=0.5,
            model='gpt-4o'
        )

        # Agent instruction
        instruction = f"""
        You are an expert thinker and problem solver. Select the most effective {self.n} prompts from the following list of prompts: {self.prompts}.
        From your selection, generate {self.n/2} pairs of parent prompts. Think carefully about how the prompts can be combined to create new ideas. Justify why you think the prompts are a good match.
        Once you have generated the pairs, breed the prompts to create new prompts. Combine the prompts in a way that enhances the original ideas and creates new insights. 
        Reminder, the prompts should instruct a language model to perfrom the task at hand.

        The output must be json code containing {self.n/2} pairs of prompts with the following format:
        {{
            "pair 1": {{
                "parent 1": "parent prompt 1",
                "parent 2": "parent prompt 2",
                "child": "child prompt",
                "pairing justification": "justification"
            }},
            "pair 2": {{
                "parent 1": "parent prompt 1",
                "parent 2": "parent prompt 2",
                "child": "child prompt",
                "pairing justification": "justification"
            }},
            ...
        }}
        """

        # Generate pairs of prompts
        model_output = llm.invoke(instruction)
        json_output = get_json(model_output)

        if json_output is None:
            json_output = model_output.content

        return json.loads(json_output)
    

class MutationAgent:
    """
    Perfrom mutations on the offspring to encourage diversity and generate unique ideas, taking inspiration from the concept of genetic mutation in biological evolution.
    Utilise the mutator prompts provided
    """

    def __init__(self, offspring: dict, mutator_prompts: list):
        self.offspring = offspring
        self.mutator_prompts = mutator_prompts

    def generate(self):
        """
        Generate n mutated ideas from offspring prompts.
        """

        # Load openai language model
        llm = ChatOpenAI(
            temperature=0.5,
            model='gpt-4o'
        )

        # Agent instruction
        instruction = f"""
        You are an expert thinker and problem solver. Generate new prompts by mutating the following child prompts: {self.offspring}. 
        Perform a mutation on each child prompt. Tailor each mutation to each prompt, using the mutator prompt from the following selection you deem most applicable: {self.mutator_prompts}.
        Reminder, the prompts should instruct a language model to perfrom the task at hand. 
        Detail how the prompts have been mutated.

        The output must be json code with the following format:
        {{
            "child prompt 1": {{
                "original prompt": "original prompt",
                "mutated prompt": "mutated child prompt",
                "details": "mutation details"
                }},
            "child prompt 2": {{
                ...
            }},
            ...
        }}
        """

        # Generate new ideas
        model_output = llm.invoke(instruction)
        json_output = get_json(model_output)

        if json_output is None:
            json_output = model_output.content

        return json.loads(json_output)
    

class NewGenerationAgent:

    def __init__(self, n: int, reviews: dict):
        self.reviews = reviews
        self.n = n

    def generate(self):

        # Load openai language model
        llm = ChatOpenAI(
            temperature=0.5,
            model='gpt-4o'
        )

        # Agent instruction
        instruction = f"""
        You are an expert thinker and problem solver. Generate a new generation of {self.n} prompts based on the following review results: {self.reviews}.
        Use the feedback from the reviewers generate improved prompts each with a unique thinking style. 
        Incorporate the positive feedback and address the negative feedback to ensure the new prompts are an improvement over the original ones.

        The output must be json code containing the new generation of prompts with the following format:
        {{
            "prompt 1": "prompt content",
            "prompt 2": "prompt content",
            ...
        }}
        """

        # Generate new generation of prompts
        model_output = llm.invoke(instruction)
        json_output = get_json(model_output)

        if json_output is None:
            json_output = model_output.content

        return json.loads(json_output)
