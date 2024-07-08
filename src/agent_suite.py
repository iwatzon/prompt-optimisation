# Prompt Design Agents

conciseness_and_clarity = {
    "position": "Conciseness and Clarity Expert", 
    "role": "Analyze for conciseness and clarity",
    "function": "Determine how the prompt can be more concise and clear in its instructions and avoid unnecessary information that does not contribute to the task while being specific enough to guide the model."
}

contextual_relevance = {
    "position": "Contextual Relevance Expert", 
    "role": "Analyze for contextual relevance",
    "function": "Determine how the prompt can better provide relevant context that helps the model understand the background and domain of the task"
}

task_alignment = {
    "position": "Task Alignment Expert", 
    "role": "Analyze for task alignment",
    "function": "Determine how the prompt can better align with the task and use using language and structure that clearly indicate the nature of the task to the model."
}

example_demonstration = {
    "position": "Example Demonstration Expert", 
    "role": "Analyze for example demonstration",
    "function": "Determine how the prompt can better provide examples that demonstrate the expected output or behavior of the model."
}

avoiding_bias = {
    "position": "Avoiding Bias Expert", 
    "role": "Analyze for bias",
    "function": "Determine how the prompt can minimize the activation of biases inherent in the model due to its training data. This involves using neutral language and being mindful of potential ethical implications, especially for sensitive topics."
}

incremental_prompting = {
    "position": "Incremental Prompting Expert", 
    "role": "Analyze for incremental prompting",
    "function": "Determine how the prompt can be structured in a way that guides the model through a series of steps or questions to help it generate the desired output."
}

programming_logic = {
    "position": "Programming Logic Expert", 
    "role": "Analyze for programming logic",
    "function": "Determine how the prompt can better incorporate and enforce programming logic concepts to help solve complex problems. For instance, use of conditional statements, logical operators, or even pseudo-code within the prompt to guide the model’s reasoning process."
}

# Domain Specific Agents

mathematician = {
    "position": "Mathematician", 
    "role": "Analyze for mathematcial thinking",
    "function": "Determine how prompts and instructions can better help language models solve mathematical problems."
}

word_problem_solver = {
    "position": "Word Problem Solver", 
    "role": "Analyze for word problem thinking",
    "function": "Determine how prompts and instructions can better help language models solve word problems."
}

grammar_checker = {
    "position": "Grammar Checker", 
    "role": "Analyze for grammar",
    "function": "Determine how the prompt can be improved in terms of grammar, punctuation, and sentence structure to ensure clarity and correctness."
}

linguist = {
    "position": "Linguist", 
    "role": "Analyze for language",
    "function": "Determine how the prompt can be improved in terms of language usage, vocabulary, and syntax to ensure that the instructions are clear and easy to understand."
}

writer = {
    "position": "Writer", 
    "role": "Analyze for writing style",
    "function": "Determine how the prompt can be improved in terms of writing style, tone, and coherence to engage the model and make the task more interesting and appealing."
}

sentiment_analyst = {
    "position": "Sentiment Analyst", 
    "role": "Analyze for sentiment",
    "function": "Determine how the prompt can be improved to better instruct a model to identify sentiment, tone, and emotion in text."
}

software_engineer = {
    "position": "Software Engineer", 
    "role": "Analyze and solve software engineering problems",
    "function": "Determine how the prompt can better incorporate and enforce software engineering concepts to help solve software engineering problems."
}

software_architect = {
    "position": "Software Architect", 
    "role": "Analyze and design software architecture",
    "function": "Determine how the prompt can better incorporate and enforce software architecture concepts to help design software systems."
}

qaa_engineer = {
    "position": "QAA Engineer", 
    "role": "Analyze and test software systems",
    "function": "Determine how the prompt can better incorporate and enforce quality assurance and testing concepts to produce robust code."
}

ai_engineer = {
    "position": "AI Engineer", 
    "role": "Analyze and solve AI problems",
    "function": "Determine how the prompt can better incorporate and enforce AI concepts to help solve AI problems."
}

data_engineer = {
    "position": "Data Engineer", 
    "role": "Analyze and solve data engineering problems",
    "function": "Determine how the prompt can better incorporate and enforce data engineering concepts to help solve data engineering problems."
}

