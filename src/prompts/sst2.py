
prefix = "Classify the sentiment of the following text as either positive or negative: "
suffix = "Please output your answer at the end as ##<your answer (No format restrictions)>"

def get_baseline_prompt():
    return prefix+"{content}\n"+suffix

def get_criteria():
    return """- The prompt MUST instruct the LLM to classify the text as either positive or negative sentiment.
- The prompt MUST include the content placeholder (this is where the text to be classified will be).
- The prompt MUST instruct the model to output the answer at the end as ##positve or ##negative with no spaces."""

def get_emotive_prompt():
    return prefix+"{content}\nThis is very important to my career.\n"+suffix

def get_CoT_prompt():
    return prefix+"{content}\nLet's think step by step.\n"+suffix