

prefix = "Complete the following function based on its signature and docstring: "
suffix = "Please output your answer at the end as ```python\n<your answer>\n```"

def get_baseline_prompt():
    return prefix+"\n```python\n{content}\n```\n"+suffix

def get_criteria():
    return """- The prompt MUST instruct the LLM to complete a function based on its signature and docstring.
- The prompt MUST include the content placeholder (this is where the function signature and docstring will be).
- The prompt MUST instruct the model to output the answer at the end as ```python\n<your answer>\n```."""

def get_emotive_prompt():
    return prefix+"\n```python\n{content}\n```\nThis is very important to my career.\n"+suffix

def get_CoT_prompt():
    return prefix+"\n```python\n{content}\n```\nLet's think step by step.\n"+suffix