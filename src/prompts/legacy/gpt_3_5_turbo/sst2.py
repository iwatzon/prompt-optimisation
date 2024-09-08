
# Times: 45.527, 13.196, 39.029
def get_authoritarian_prompts():
    return ["""Classify the sentiment of the following text as either positive or negative.

{content}

Output your answer as ##positive or ##negative at the end with no spaces.""",
"""Classify the sentiment of the text in {content} as either positive or negative. Provide your answer at the end as ##positive or ##negative with no spaces.""",
"""Classify the sentiment of the following text as either positive or negative: {content}
Please output your answer at the end as ##positive or ##negative with no spaces."""
]

# Times: 7.222, 10.222, 9.600
def get_market_prompts():
    return ["""Classify the sentiment of the following text as either positive or negative: {content}
Analyze the sentiment and provide your answer at the end as ##positive or ##negative with no spaces.""",
"""Classify the sentiment of the following text as either positive or negative. Please output your answer at the end in the format ##positive or ##negative with no spaces. {content}""",
"""Classify the sentiment of the following text as either positive or negative: {content}. Ensure to consider the overall tone and context before making your classification.
Please provide your answer at the end as ##positive or ##negative with no spaces."""
]

# Times: 41.432, 44.707, 44.937
def get_hierarchical_prompts():
    return ["""Analyze the sentiment of the following text and classify it as either positive or negative. {content} Provide your answer at the end using ##positive or ##negative without any additional characters.""",
"""Analyze the following text and classify its sentiment as either positive or negative. Explore the emotional journey of the text, identifying shifts in emotions and intensity levels. Interpret the underlying emotional intent behind the emotive language used. Consider how cultural or contextual influences shape the sentiment. Output the answer as ##positive or ##negative with no spaces.

Content Placeholder: {content}""",
"""Analyze the sentiment of the following text as either positive or negative. {content} Please indicate your classification at the end using ##positive or ##negative without any spaces."""
    ]