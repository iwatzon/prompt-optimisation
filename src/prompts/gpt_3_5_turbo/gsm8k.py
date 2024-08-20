
# Times: 37.035, 6.299, 34.962
def get_authoritarian_prompts():
    return ["""Prompt: 
{content}
Solve the following maths word problem and output your answer at the end as ##<your answer (arabic numerals)>""",
"""Prompt: Solve the following maths word problem: {content} Output your answer at the end as ##<your answer (arabic numerals)>""",
"""Solve the following maths word problem: 
{content}
Please provide your answer at the end as ##<your answer (arabic numerals)> without any spaces. After giving the answer, explain the steps or reasoning behind the solution process. Additionally, consider exploring alternative problem-solving methods or creative approaches."""
    ]

# Times: 10.195, 7.989, 27.758
def get_market_prompts():
    return ["""**Task: Math Word Problem Solving**

Please solve the following math word problem and provide your answer at the end in the format ##<your answer (arabic numerals)> with no spaces.

**Problem:** {content}

*Remember to show your calculations and reasoning clearly in your response.*""",
"""Please solve the following math word problem and provide your answer at the end in the format ##<your answer (arabic numerals)> without any spaces.

{content}""",
"""Solve the following math word problem and provide your answer at the end in the format ##{{your answer (arabic numerals)}} without any spaces.

{content} Answer in the format ##{{your answer (arabic numerals)}} without any spaces."""
    ]

# Times: 51.337, 52.667, 48.428
def get_hierarchical_prompts():
    return ["""Solve the following math word problem that includes a unique twist or challenge: {content}
After solving the problem, explain the reasoning behind each step taken to arrive at the solution.
Please provide your answer at the end in the format ##<your answer (arabic numerals)> without any spaces.""",
"""Solve the following maths word problem: {content} Calculate the answer and provide it at the end in the format ##<your answer (arabic numerals)>
""",
"""Please solve the following math word problem: {content} Please output your answer at the end as ##<your answer (arabic numerals)>"""
]