
# Times: 177.748, 38.277, 32.951
def get_authoritarian_prompts():
    return ['''Solve the following maths word problem: {content} Output the answer as ##<your answer (arabic numerals)>. For example, if the problem is 'If a train travels 60 miles in 1 hour, how far will it travel in 3 hours?', the output should be ##180. Please solve the problem step-by-step before providing the final answer.''',
'''Solve the following math word problem: {content} Ensure to output the answer at the end in the format ##<your answer (arabic numerals)> with no spaces.''',
'''Solve the following math word problem: {content}
Provide the answer in the format ##<your answer (arabic numerals)>'''
    ]

# Times: 147.139, 194.302, 117.576
def get_market_prompts():
    return ['''Solve the following math word problem:
{content}
Output your answer as ##<your answer (arabic numerals)> with no spaces. For example, if the answer is 42, write it as ##42. Show all steps clearly.

**Example 1:**
**Problem:** If a train travels 60 miles in 1.5 hours, what is its average speed in miles per hour?
**Solution:** Divide the total distance by the total time: 60 miles / 1.5 hours = 40 miles per hour.
**Output:** ##40

**Example 2:**
**Problem:** A rectangle has a length of 10 meters and a width of 5 meters. What is its area in square meters?
**Solution:** Multiply the length by the width: 10 meters * 5 meters = 50 square meters.
**Output:** ##50

**Example 3:**
**Problem:** A store is having a 20% off sale. If an item originally costs $50, what is the sale price?
**Solution:** Calculate 20% of $50: 0.20 * $50 = $10. Subtract this from the original price: $50 - $10 = $40.
**Output:** ##40''',
'''Solve this math problem:

{content}

Identify known values, set up equations, and solve for the unknown.

**Example 1**:
A train travels 60 miles in 1.5 hours. What is its average speed in miles per hour?
- Distance = 60 miles, Time = 1.5 hours
- Speed = Distance / Time
- Speed = 60 / 1.5 = 40 miles per hour
- Final answer: ##40

**Example 2**:
A car rental company charges a flat fee of $50 plus $0.20 per mile. If a customer has $90, how many miles can they drive?
- Flat fee = $50, Cost per mile = $0.20, Budget = $90
- 50 + 0.20 * Miles = 90
- 0.20 * Miles = 40
- Miles = 40 / 0.20 = 200 miles
- Final answer: ##200

Output your final answer as ##<your answer (arabic numerals)> with no spaces.''',
'''Solve the following math problem step-by-step:
{content}

1. Identify key information and variables:
   - Look for numbers, units, and relationships between variables.
   - Write down any given equations or formulas.

2. Break the problem into smaller parts and solve each part:
   - Divide the problem into manageable sections.
   - Solve each section individually, ensuring to check your work for accuracy.

3. Label each step clearly:
   - Use labels such as "Step 1," "Step 2," etc.
   - Provide a brief description of what is being done in each step.

4. Combine results for the final answer:
   - Ensure all intermediate results are correct.
   - Combine the results logically to arrive at the final answer.

5. Output the final answer as ##<your answer (arabic numerals)> with no spaces.'''
    ]

# Times: 65.090, 40.305, 24.223
def get_hierarchical_prompts():
    return ['''Solve the following math word problem: 
{content}
Output the answer at the end as ##<your answer (arabic numerals)>''',
'''Solve the following maths word problem:
{content}

1. Identify key information.
2. Perform necessary calculations.
3. Double-check your work.

Output your final answer as ##<your answer (arabic numerals)> with no spaces.''',
'''Solve the following maths word problem step-by-step:
{content}
Output the final answer as ##<your answer (arabic numerals)> with no spaces.'''
]