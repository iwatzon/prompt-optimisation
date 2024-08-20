class GSM8KPrompts():

   def __init__(self):
      pass
    
   # Max time:  328.93039321899414
   # Min time:  44.54635500907898
   # Average time:  137.77577815055847
   def get_authoritarian_prompts_0(self):
      return [
'''{content}
Please solve the math word problem in {content}. Format your final answer as ##<your answer (arabic numerals)>.

Examples:
"What is 5 plus 3?" -> ##8
"What is 12 divided by 4?" -> ##3''',
'''As a Math Tutor, your task is to solve the following math word problem and provide the answer in a specific format. Math word problems help students apply mathematical concepts to real-world scenarios. 

Follow these steps to solve the problem:
1. Read the problem carefully.
2. Identify the mathematical operation required (e.g., addition, subtraction, multiplication, division).
3. Perform the calculation step-by-step.
4. Format your answer as ##<your answer (arabic numerals)>.

Example 1:
Problem: If you have 3 apples and you buy 2 more, how many apples do you have in total?
Solution: 3 + 2 = 5
Output: ##5

Example 2:
Problem: A car travels 60 miles per hour. How far will it travel in 3 hours?
Solution: 60 miles/hour * 3 hours = 180 miles
Output: ##180

Example 3:
Problem: If you divide 20 candies equally among 4 children, how many candies does each child get?
Solution: 20 / 4 = 5
Output: ##5

Now, solve the given problem and output your answer as ##<your answer (arabic numerals)>.''',
'''Please read the following content and solve the maths word problem:

{content}

Steps to solve the problem:
1. Understand the problem.
2. List given and unknown facts.
3. Organize the facts.
4. Solve the problem.

Output your answer in this format: ##<your answer (arabic numerals)>

Examples:

Example 1:
Content: "Calculate the sum of 15 and 27."
Steps:
1. Problem: Find the sum of 15 and 27.
2. Facts: 15, 27
3. Organized: 15 + 27
4. Solution: 15 + 27 = 42
Output: ##42

Example 2:
Content: "If a train travels 60 miles per hour for 3 hours, how far does it travel?"
Steps:
1. Problem: Find the distance traveled by the train.
2. Facts: Speed = 60 miles/hour, Time = 3 hours
3. Organized: Distance = Speed * Time
4. Solution: Distance = 60 * 3 = 180 miles
Output: ##180

Example 3:
Content: "A rectangle has a length of 10 units and a width of 5 units. What is its area?"
Steps:
1. Problem: Find the area of the rectangle.
2. Facts: Length = 10 units, Width = 5 units
3. Organized: Area = Length * Width
4. Solution: Area = 10 * 5 = 50 square units
Output: ##50''',
'''Solve the following maths word problem and provide your answer in the format ##<your answer>.

Content: {content}

Example:
Content: "If you have 3 apples and you buy 2 more, how many apples do you have in total?"
Answer: ##5

Your answer:''',
'''Please solve the following math word problem and provide your answer at the end in the specified format.

{content}

Your answer should be enclosed within `##` and presented in Arabic numerals with no spaces. For example, if the answer is 42, write it as ##42##.

Please output your answer at the end as ##<your answer (arabic numerals)>.'''
        ]
    
   # Max time:  156.38128900527954
   # Min time:  93.79756617546082
   # Average time:  122.59880180358887
   def get_authoritarian_prompts_1(self):
      return[
'''Solve the problem step-by-step, showing all calculations. Output your final answer at the end as ##<your answer (arabic numerals)>.

**Example 1 (Simple):**
Math Word Problem: "If you have 3 apples and you buy 2 more, how many apples do you have in total?"
- Identify the initial number of apples: 3
- Add the number of apples bought: 3 + 2
- Calculate the total: 5
- Final Answer: ##5

**Example 2 (Intermediate):**
Math Word Problem: "A train travels 60 miles per hour. How long does it take to travel 240 miles?"
- Identify the speed of the train: 60 miles per hour
- Identify the distance: 240 miles
- Calculate the time by dividing distance by speed: 240 / 60
- Perform the calculation: 4 hours
- Final Answer: ##4

{content}''',
'''**Math Tutor Task**

As a math tutor, you are tasked with solving the following math problem:

{content}

---

**Examples to Guide You:**

1. **Problem:** Jane has 10 bananas. She eats 2 and buys 4 more. How many bananas does she have now?
   - **Calculation:** 10 (initial) - 2 (eaten) + 4 (bought) = 12
   - **Final answer:** ##12

2. **Problem:** Tom has 15 dollars. He spends 5 dollars on snacks and finds 10 dollars on the street. How much money does Tom have now?
   - **Calculation:** 15 (initial) - 5 (spent) + 10 (found) = 20
   - **Final answer:** ##20

---

**Final Instruction:**

Write your final answer in the format: ##<your answer in digits>''',
'''Examples:
1. Basic Arithmetic: 
   Problem: "If Sarah has 5 apples and buys 3 more, how many apples does she have?"
   Steps to solve:
   - Step 1: Identify initial quantity: 5 apples
   - Step 2: Identify additional quantity: 3 apples
   - Step 3: Add the quantities: 5 + 3 = 8
   The answer is ##8.

2. Subtraction: 
   Problem: "Tom started with 12 candies and gave away 4. How many candies does Tom have now?"
   Steps to solve:
   - Step 1: Identify initial quantity: 12 candies
   - Step 2: Identify quantity given away: 4 candies
   - Step 3: Subtract the quantities: 12 - 4 = 8
   The answer is ##8.

3. Multiplication: 
   Problem: "A box contains 6 packets of cookies, each packet has 4 cookies. How many cookies are there in total?"
   Steps to solve:
   - Step 1: Identify number of packets: 6
   - Step 2: Identify cookies per packet: 4
   - Step 3: Multiply the quantities: 6 * 4 = 24
   The answer is ##24.

4. Division: 
   Problem: "You have 20 chocolates and want to share them with 5 friends equally. How many chocolates will each friend get?"
   Steps to solve:
   - Step 1: Identify total chocolates: 20
   - Step 2: Identify number of friends: 5
   - Step 3: Divide the quantities: 20 / 5 = 4
   The answer is ##4.

5. Combined Operations: 
   Problem: "If you buy 3 packs of pencils, each containing 10 pencils, and give away 5, how many pencils do you have?"
   Steps to solve:
   - Step 1: Identify packs of pencils bought: 3
   - Step 2: Pencils per pack: 10
   - Step 3: Calculate total pencils: 3 * 10 = 30
   - Step 4: Subtract pencils given away: 30 - 5 = 25
   The answer is ##25.

{content}

After solving the problem, write your answer as ##<answer>. For example, for an answer of 8, write ##8.
''',
'''Please solve the following maths word problem:

{content}

Output your answer at the end as ##<your answer (arabic numerals)> with no spaces.''',
'''Carefully read the maths problem in {content}. Identify the necessary information, solve the problem step-by-step, and format your final answer as ##<your answer (arabic numerals)>.'''
        ]
    
   # Max time:  258.10102701187134
   # Min time:  19.70585298538208
   # Average time:  86.7271285533905
   def get_market_prompts_0(self):
      return[
'''Solve the following maths word problem: {content}
Please ensure your answer is formatted exactly as ##<your answer (arabic numerals)> with no spaces. For example, if the answer is 42, you should write it as ##42.''',
'''You are an experienced: Word_Problem_Solver. Your core principles are:
- Read the problem carefully to understand what is being asked.
- List the given and unknown facts.
- Organize the problem and facts clearly.
- Consider multiple approaches to find the solution.

Follow these steps to solve the math word problem:

1. **Read the Problem Carefully:** Understand what you need to find.
2. **List the Facts:** Identify and list the given and unknown facts.
3. **Organize the Problem:** Rewrite the problem and facts clearly.
4. **Consider Multiple Approaches:** Think of different ways to solve the problem and choose the best method.

### Example 1 (Simple Problem):
**Problem:** John has 3 apples. He buys 2 more apples. How many apples does he have now?

1. **Read the Problem Carefully:** Find the total number of apples John has after buying more.
2. **List the Facts:**
   - Given: John has 3 apples.
   - Given: John buys 2 more apples.
   - Unknown: Total number of apples John has now.
3. **Organize the Problem:**
   - Initial apples: 3
   - Additional apples: 2
   - Total apples: 3 + 2
4. **Consider Multiple Approaches:**
   - Addition: 3 + 2 = 5

**Answer:** ##5

### Example 2 (Complex Problem):
**Problem:** A car travels 60 miles in 1 hour. How long will it take to travel 180 miles at the same speed?

1. **Read the Problem Carefully:** Find the time to travel 180 miles at a constant speed.
2. **List the Facts:**
   - Given: Speed of the car is 60 miles per hour.
   - Given: Distance to travel is 180 miles.
   - Unknown: Time to travel 180 miles.
3. **Organize the Problem:**
   - Speed: 60 miles/hour
   - Distance: 180 miles
   - Time = Distance / Speed
4. **Consider Multiple Approaches:**
   - Division: 180 miles / 60 miles/hour = 3 hours

**Answer:** ##3

Solve the following math word problem:

{content}

Please output your answer at the end as ##<your answer (arabic numerals)>''',
'''Solve the following maths word problem: {content}
Please output your answer at the end as ##<your answer (arabic numerals)>.
For example, if the answer is 42, write it as ##42.''',
'''Solve the following maths word problem:

{content}

Please ensure your final answer is provided at the end in the format: ##<your answer (arabic numerals)>''',
'''You are an experienced: Word_Problem_Solver. Your core principles are:
- Read the problem carefully.
- List given facts and unknowns.
- Organize the facts clearly.
- Estimate the answer.
- Use correct mathematical operations.
- Double-check calculations.

Follow these steps to solve the problem:

1. Identify the question.
2. List given facts and unknowns.
3. Organize the facts.
4. Estimate the answer.
5. Solve using correct operations.
6. Double-check calculations.
7. Output your answer as ##<your answer (arabic numerals)> with no spaces.

**Example 1:**

**Problem:** A farmer has 10 apples. He gives 3 apples to his neighbor and then buys 5 more apples. How many apples does the farmer have now?

1. **Question:** How many apples does the farmer have now?
2. **Facts:**
   - Initial apples: 10
   - Apples given away: 3
   - Apples bought: 5
3. **Organized facts:**
   - Initial apples: 10
   - Apples after giving away: 10 - 3 = 7
   - Apples after buying more: 7 + 5 = 12
4. **Estimate:** Around 10 apples.
5. **Solution:** 10 - 3 + 5 = 12
6. **Double-Check:** 10 - 3 = 7, 7 + 5 = 12
7. **Output:** ##12

**Example 2:**

**Problem:** Sarah has twice as many marbles as Tom. If Tom has 8 marbles, how many marbles does Sarah have?

1. **Question:** How many marbles does Sarah have?
2. **Facts:**
   - Tom's marbles: 8
   - Sarah's marbles: 2 times Tom's marbles
3. **Organized facts:**
   - Tom's marbles: 8
   - Sarah's marbles: 2 * 8 = 16
4. **Estimate:** Around 16 marbles.
5. **Solution:** 2 * 8 = 16
6. **Double-Check:** 2 * 8 = 16
7. **Output:** ##16

**Example 3:**

**Problem:** A recipe requires 3/4 cup of sugar. If you want to make half of the recipe, how much sugar do you need?

1. **Question:** How much sugar is needed for half of the recipe?
2. **Facts:**
   - Full recipe sugar: 3/4 cup
   - Fraction of the recipe: 1/2
3. **Organized facts:**
   - Full recipe sugar: 3/4 cup
   - Sugar for half the recipe: (3/4) * (1/2) = 3/8 cup
4. **Estimate:** Around 0.375 cups.
5. **Solution:** (3/4) * (1/2) = 3/8
6. **Double-Check:** (3/4) * (1/2) = 3/8
7. **Output:** ##0.375

{content}

Please output your answer at the end as ##<your answer (arabic numerals)> with no spaces.'''
        ]
    
   # Max time:  228.35074615478516
   # Min time:  35.87507200241089
   # Average time:  133.8841024875641
   def get_market_prompts_1(self):
      return[
'''Your task is to solve the following maths word problem. Please carefully read the problem and provide a detailed solution. Your solution should show all the steps necessary to arrive at the final answer. Make sure to perform any necessary calculations accurately.

**Example 1 (Simple):**
Problem: John has 3 apples. He buys 2 more apples. How many apples does John have now?
Steps:
1. Note the initial number of apples.
2. Note the additional apples bought.
3. Add the two quantities together.
Solution: 
- John starts with 3 apples.
- He buys 2 more apples.
- The total number of apples is 3 + 2.
- Therefore, John has 5 apples.

**Example 2 (Moderate):**
Problem: A car travels at a speed of 60 miles per hour. How long will it take to travel 180 miles?
Steps:
1. Note the car's speed.
2. Note the total distance to travel.
3. Use the formula: Time = Distance / Speed.
Solution:
- The car's speed is 60 miles per hour.
- The total distance to travel is 180 miles.
- Time taken = Distance / Speed = 180 miles / 60 miles per hour.
- Therefore, it will take 3 hours.

**Example 3 (Complex):** 
Problem: If a rectangle has a length of 10 cm and the width is half of the length, what is the area of the rectangle?
Steps:
1. Note the length of the rectangle.
2. Calculate the width as half of the length.
3. Use the formula: Area = Length x Width.
Solution:
- The length of the rectangle is 10 cm.
- The width is half of the length, so the width is 10 cm / 2 = 5 cm.
- Area of the rectangle = length x width = 10 cm x 5 cm = 50 square cm.
- Therefore, the area of the rectangle is 50 square cm.

Now, solve the problem given below:

{content}

Please output your answer at the end as ##<your answer (arabic numerals)>''',
'''You are required to solve the following maths word problem thoroughly. Make sure to show your work for clarity and comprehension.

For example:
If the problem was:
"John has 5 apples, and he buys 7 more apples. How many apples does John have in total?"

Your solution should be:
John starts with 5 apples and buys 7 more. Therefore, the total number of apples John has is 5 + 7 = 12.

At the end of your solution, please output your answer as ##12 with no spaces.

Please follow this format for the following problem:

{content}

Please output your answer at the end as ##<your answer (arabic numerals)> with no spaces.''',
'''Solve this maths problem:

1. Read the problem slowly and carefully. Understand what the problem is asking you to find.
2. Break the problem into parts. List the given information, including units, and identify the unknowns. This helps in visualizing the problem clearly.
3. Rewrite the problem and facts in a more organized manner to ensure clarity.
4. Consider multiple approaches for solving the problem, including any special cases or different scenarios. Choose the most efficient one.
5. Calculate the solution step-by-step in detail, documenting each part of your process. Use units in your intermediate steps to maintain clarity.
6. Double-check your calculations thoroughly. Ensure all details have been considered and the solution is accurate and reliable.
7. Format the answer as ##<your answer (arabic numerals)> with no spaces.

### Example 1:
- **Problem:** A train travels 60 miles in 2 hours. What is its speed in miles per hour?
- **Details:** distance = 60 miles, time = 2 hours.
- **Calculation:** speed = distance / time = 60 miles / 2 hours = 30 miles per hour.
- **Answer:** ##30

### Example 2:
- **Problem:** A garden has 3 rows of 5 flowers each. How many flowers are there in total?
- **Details:** rows = 3, flowers per row = 5.
- **Calculation:** total flowers = rows * flowers per row = 3 rows * 5 flowers per row = 15 flowers.
- **Answer:** ##15

Solve this problem:

{content}''',
'''To solve the math word problem effectively, follow these steps:

1. **Read Carefully**: Read the problem slowly and carefully to understand what it is asking you to find.
2. **Identify Facts and Unknowns**: Identify and list the given facts and the unknowns.
3. **Organize the Information**: Rewrite the problem and facts in a more organized manner, if necessary.
4. **Estimate the Solution**: Develop an initial guess of the answer. (This helps in verifying the plausibility of the final result.)
5. **Consider Multiple Approaches**: Think about different ways to solve the problem and select the most straightforward and effective method.
6. **Perform Calculations**: Use correct mathematical operators (addition, subtraction, multiplication, division) to perform mathematical calculations.
7. **Double-Check Calculations**: Review each calculation step to ensure accuracy.

Here are some examples of how to solve a math word problem and how to format your answer:

**Example 1**:
**Problem**: John has 3 apples, and he buys 5 more. How many apples does John have now?
**Solution**:
   1. **Given**: John has 3 apples, buys 5 more apples.
   2. **Unknown**: Total apples John has.
   3. **Estimate**: Slightly less than 10 apples.
   4. **Calculation**: 3 + 5 = 8
   5. **Double-check**: 3 + 5 indeed equals 8.

**Answer**: ##8

**Example 2**:
**Problem**: If a car travels 60 miles per hour for 3 hours, how far does it travel?
**Solution**:
   1. **Given**: Speed = 60 mph, Time = 3 hours.
   2. **Unknown**: Distance traveled.
   3. **Estimate**: About 180 miles.
   4. **Calculation**: 60 * 3 = 180
   5. **Double-check**: 60 * 3 indeed equals 180.

**Answer**: ##180

**Example 3**:
**Problem**: Sarah buys 3 packs of pencils, each with 12 pencils. She gives away 10. How many does she have?
**Solution**:
   1. **Given**: 3 packs, 12 pencils each, gives away 10 pencils.
   2. **Unknown**: Pencils remaining.
   3. **Estimate**: Around 30 pencils minus 10, so about 20 pencils.
   4. **Calculation**: 3 * 12 - 10 = 26
   5. **Double-check**: 36 - 10 indeed equals 26.

**Answer**: ##26

Now, solve the following problem: {content}

Format the answer as ##<your answer (arabic numerals)> with no spaces.
''',
'''**Task:** Solve the math word problem below. The examples provided cover different types of mathematical problems, including single or multiple operations.

**Examples:**

**Example 1 (Addition):**
Problem: Jane has 3 apples. She buys 5 more. How many now?
Solution: 3 + 5 = 8
Output: ##8##

**Example 2 (Multiplication):**
Problem: A car travels 60 miles/hour. How far in 3 hours?
Solution: 60 * 3 = 180
Output: ##180##

**Example 3 (Perimeter):**
Problem: Sarah's garden is 8m long and 6m wide. How many meters of fencing?
Solution: 2 * (8 + 6) = 28
Output: ##28##

**Example 4 (Division):**
Problem: John has a 9m rope. Cuts into 3m pieces. How many pieces?
Solution: 9 / 3 = 3
Output: ##3##

**Example 5 (Percentage):**
Problem: A jacket is 25% off $80. What is the sale price?
Solution: $80 - 25% of $80 = $60
Output: ##60##

**Example 6 (Multi-Step Problem):**
Problem: A school sold 50 tickets to a play. Adult tickets are $10 each and child tickets are $5 each. If the total amount collected was $350, how many adult tickets were sold?
Solution: Let A be the number of adult tickets and C be the number of child tickets.
A + C = 50
10A + 5C = 350
Solving these equations: A = 20, C = 30
Output: ##20##

Now, solve this problem: {content}  
Output your answer as ##<your answer (arabic numerals)>.'''
      ]
    
   # Max time:  96.04924631118774
   # Min time:  40.32485890388489
   # Average time:  55.92056860923767
   def get_hierarchical_prompts_0(self):
      return[
'''Solve the maths word problem in {content}. Output your answer as ##<your answer (arabic numerals)> with no spaces.''',
'''{content}

Please follow these steps to solve the problem:

1. **Read the problem carefully** to understand what is being asked.
2. **List the given facts** and **identify the unknowns**.
3. **Rewrite the problem** in a more organized manner if necessary.
4. **Make an initial estimate** of the answer.
5. **Consider multiple approaches** to solve the problem.
6. **Use mathematical operators correctly** in your calculations.
7. **Double-check your calculations** to ensure accuracy.
8. **Solve the problem** and **output the answer** at the end as ##<your answer (arabic numerals)> with no spaces.
''',
'''Solve the following math word problem: {content}
Output your answer at the end as ##<your answer (arabic numerals)> with no spaces.''',
'''As a Math Solver, your task is to solve the following maths word problem:

{content}

Please solve the problem and output your answer at the end as ##<your answer (arabic numerals)> with no spaces.
```''',
'''You will be given a maths word problem in {content}. Carefully solve the problem and ensure your answer is accurate. Output your answer as ##<your answer (arabic numerals)> with no spaces.'''
        ]
    
   # Max time:  50.16527009010315
   # Min time:  41.16860795021057
   # Average time:  46.46960501670837
   def get_hierarchical_prompts_1(self):
      return[
'''You will be given a math word problem in the `{content}` placeholder. Solve it, and ensure you reflect the correct numerical solution. See the example below for guidance:

[Example Input: "If three apples cost $1.50, how much do five apples cost?" Example Output: ##2.50]

Once you solve the problem, output your answer as ##<your answer (arabic numerals)> with no spaces.''',
'''{content}\\n\\nSolve the following maths word problem. Show your step-by-step workings clearly. Output your final answer at the end as ##<your answer (arabic numerals)> with no spaces.''',
'''{content}
As a maths problem solver, solve the word problem above and output your answer as ##<your answer (arabic numerals)> with no spaces.
```''',
'''Solve the following maths word problem:

{content}

Provide the answer as ##<your answer (arabic numerals)> without spaces.''',
'''Solve the following maths word problem:
{content}

Logically go through each step. Output your final answer as ##<your answer (arabic numerals)> with no spaces.'''
        ]
    
    
