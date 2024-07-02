# Pre-defined agents

# Agents with specilaised jobs
mathematician = {
    "position": "Mathematician", 
    "role": "Analyze and solve mathematical problems",
    "function": "Provide feedback on how the prompt can better incorporate and enforce mathematical thinking and problem solving techniques to help solve mathematical problems."
}

linguist = {
    "position": "Linguist", 
    "role": "Analyze linguistic features",
    "function": "Determine how the syntax, formatting and structure of the prompt can be improved to help instruct a large language model."
}

prompt_engineer = {
    "position": "Prompt Engineer", 
    "role": "Analyze prompts for best practices",
    "function": "Determine how the prompt can adhere to best practices for writing prompts. Encourage the use of appropriate prompting techniques including zero-shot, few-shot, chain-of-thought, self-consistency, generate knowledge and more."
}

software_engineer = {
    "position": "Software Engineer", 
    "role": "Analyze software engineering problems",
    "function": "Determine how the prompt can better incorporate and enforce software engineering concepts to help solve software engineering problems."
}

# Agents specialising in design aspects: http://arxiv.org/abs/2312.16171
conciseness_and_clarity = {
    "position": "Conciseness and Clarity", 
    "role": "Analyze for conciseness and clarity",
    "function": "Determine how the prompt can be more concise and clear in its instructions and avoid unnecessary information that does not contribute to the task while being specific enough to guide the model."
}

contextual_relevance = {
    "position": "Contextual Relevance", 
    "role": "Analyze for contextual relevance",
    "function": "Determine how the prompt can better provide relevant context that helps the model understand the background and domain of the task"
}

task_alignment = {
    "position": "Task Alignment", 
    "role": "Analyze for task alignment",
    "function": "Determine how the prompt can better align with the task and use using language and structure that clearly indicate the nature of the task to the model."
}

example_demonstration = {
    "position": "Example Demonstration", 
    "role": "Analyze for example demonstration",
    "function": "Determine how the prompt can better provide examples that demonstrate the expected output or behavior of the model."
}

avoiding_bias = {
    "position": "Avoiding Bias", 
    "role": "Analyze for bias",
    "function": "Determine how the prompt can minimize the activation of biases inherent in the model due to its training data. This involves using neutral language and being mindful of potential ethical implications, especially for sensitive topics."
}

incremental_pormpting = {
    "position": "Incremental Prompting", 
    "role": "Analyze for incremental prompting",
    "function": "Determine how the prompt can be structured in a way that guides the model through a series of steps or questions to help it generate the desired output."
}

programming_logic = {
    "position": "Programming Logic", 
    "role": "Analyze for programming logic",
    "function": "Determine how the prompt can better incorporate and enforce programming logic concepts to help solve complex problems. For instance, use of conditional statements, logical operators, or even pseudo-code within the prompt to guide the model’s reasoning process."
}



