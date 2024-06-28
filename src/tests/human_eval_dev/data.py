# https://github.com/openai/human-eval/blob/master/human_eval/data.py

import json
from typing import Iterable, Dict
import os

# set root to source directory
HUMAN_EVAL = "/Users/iwatson/Documents/Research Project/prompt-optimisation/src/data/code_generation/HumanEval.jsonl"

def read_problems(evalset_file: str = HUMAN_EVAL):
    return {task["task_id"]: task for task in stream_jsonl(evalset_file)}

def stream_jsonl(filename: str):
    """
    Parses each jsonl line and yields it as a dictionary
    """
    with open(filename, "r") as fp:
        for line in fp:
            if any(not x.isspace() for x in line):
                yield json.loads(line)

def write_jsonl(filename: str, data: Iterable[Dict], append: bool = False):
    """
    Writes an iterable of dictionaries to jsonl
    """
    if append:
        mode = 'ab'
    else:
        mode = 'wb'
    filename = os.path.expanduser(filename)
    with open(filename, mode) as fp:
        for x in data:
            fp.write((json.dumps(x) + "\n").encode('utf-8'))