# https://github.com/openai/human-eval/blob/master/README.md

from langchain_core.pydantic_v1 import BaseModel, Field
from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from tqdm import tqdm

from data import read_problems, write_jsonl

import re

def extract_code_blocks(text):
    """
    Extracts code blocks from markdown text.
    """
    # This regex matches content between triple backticks
    code_blocks = re.findall(r'```python\n(.*?)\n```', text, re.DOTALL)
    return code_blocks

class Response(BaseModel):
    """Final response to the prompt"""
    code: str = Field(description="Code block generated in response to the prompt")

def generate_one_completion(base_prompt: str, task_prompt: str, temp: float, model: str) -> Response:
    """
    Generates code completion for a given task prompt.
    """
    llm = ChatOpenAI(
        temperature=temp,
        model=model
    )
    pydantic_parser = PydanticOutputParser(pydantic_object=Response)
    prompt = PromptTemplate(
        template="{base_prompt}:\n{format_instructions}\n{task}\n",
        input_variables=["task"],
        partial_variables={"format_instructions": pydantic_parser.get_format_instructions()},
    )
    chain = prompt | llm | pydantic_parser
    completion = chain.invoke({"base_prompt": base_prompt, "task": task_prompt})
    return completion.code

def generate_llm_outputs(base_prompt: str, sample_size: int, temp: float = 0.0, model: str = "gpt-4o"):
    """
    Generates completions for all tasks in the human evaluation set.
    """
    from itertools import islice

    problems = read_problems()
    samples = [
        dict(task_id=task_id, completion=generate_one_completion(base_prompt, problems[task_id]["prompt"], temp, model))
        for task_id in tqdm(dict(islice(problems.items(), sample_size)))
    ]
    write_jsonl("llm_outputs.jsonl", samples)