
# Times: 72.062, 65.115, 62.072
def get_authoritarian_prompts():
    return ['''Please solve the following math word problem: {content}. 
- Identify key numbers and relationships, and determine what is unknown. 
- Organize the problem clearly, visualize it if helpful (e.g., drawing a diagram or creating a table), and formulate an equation if applicable. 
- Consider creative and unconventional approaches to the solution, reflecting on the context and implications of your answer. 
- Identify any assumptions you are making and think about how different mathematical concepts might interact. 
- Approach the problem iteratively, refining your solution as needed. 
Finally, output your answer as ##<your answer (arabic numerals)> with no spaces and no additional text.''',
'''Solve the following maths word problem: {content}. Break down the problem into steps, explore different methods or creative approaches if applicable, and explain your reasoning clearly. Consider outlining your thought process and double-check your calculations for accuracy. Reflect on your solution process if it adds value. Finally, output your answer as ##<your answer (arabic numerals)> with no spaces.''',
'''Please solve the following math word problem: {content}. 
- List the known and unknown facts.
- Rewrite the problem in an organized manner.
- Consider different approaches and explain your reasoning.
- Explain your solution in up to 3 sentences.
- Think about any special cases or different interpretations of the problem.
Finally, output your answer at the end as ##<your answer (arabic numerals)> with no spaces and no additional text.'''
    ]

# Times: 21.881, 108.220, 33.712
def get_market_prompts():
    return ['''Please solve the following maths word problem: {content}. To help you understand the task, consider these examples of varying complexities:

1. Example 1: If a train travels 60 miles in 1 hour, how far will it travel in 3 hours? The answer is 180.
2. Example 2: Sarah has 5 apples, and she buys 3 more. How many apples does she have now? The answer is 8.
3. Example 3: A rectangle has a length of 10 cm and a width of 4 cm. What is the area of the rectangle? The answer is 40.
4. Example 4: A store is having a sale where all items are 20% off. If a shirt costs $50, how much will it cost after the discount? The answer is 40.
5. Example 5: If a car travels 150 miles in 2.5 hours, what is its average speed in miles per hour? The answer is 60.
6. Example 6: A recipe requires 2 cups of flour for every 3 cups of sugar. If you want to use 9 cups of sugar, how many cups of flour do you need? The answer is 6.

Please output your answer at the end as ##<your answer (arabic numerals)> with no spaces and no additional text.''',
'''As a math tutor, solve the maths word problem: {content}. Start with an estimate based on the numbers. Break the problem into smaller parts and explore strategies. After calculating, check your steps for correct math operations. Reflect on the reasonableness of your final answer. If you find discrepancies, reassess your approach. Present your final answer as ##<your answer (arabic numerals)> with no spaces.''',
'''Please solve the following maths word problem: {content}. To help you understand the task, consider the following diverse examples:

1. Example 1: If a train travels 60 miles in 1 hour, how far will it travel in 3 hours? The answer is 180 miles. Output: ##180
2. Example 2: Sarah has 5 apples, and she buys 3 more. How many apples does she have now? The answer is 8 apples. Output: ##8
3. Example 3: A rectangle has a length of 10 cm and a width of 4 cm. What is the area of the rectangle? The answer is 40 square cm. Output: ##40
4. Example 4: If a shirt originally costs $50 and is on sale for 20% off, what is the sale price? The answer is $40. Output: ##40
5. Example 5: A recipe requires 2 cups of flour for every 3 cups of sugar. If you have 6 cups of sugar, how many cups of flour do you need? The answer is 4 cups of flour. Output: ##4

Please ensure your answer is clearly stated at the end as ##<your answer (arabic numerals)> with no spaces and no additional text or explanations. It is encouraged to show your reasoning or calculations step-by-step before arriving at the final answer.'''
    ]

# Times: 51.487, 87.173, 87.304
def get_hierarchical_prompts():
    return ['''Please solve the following maths word problem: {content}. Read the problem carefully and outline your reasoning and calculations step-by-step. Conclude with your answer formatted as ##<your answer (arabic numerals)> without spaces.''',
'''Solve the following maths word problem: {content}.
Present your final answer as ##<your answer (arabic numerals)> with no spaces.''',
'''Solve the following maths word problem: 
{content}
Please output your answer at the end as ##<your answer (arabic numerals)> without any spaces.'''
    ]