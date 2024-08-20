
# Times: 354.685, 197.310, 202.997
def get_authoritarian_prompts():
    return ["""Assume the role of a Mathematical Detective solving a numerical mystery. Your mission is to unravel this math word problem:

{content}

Investigation steps:
1. Decode the central question
2. Gather evidence (facts and unknowns)
3. Sketch a mental crime scene (visualize the problem)
4. Hypothesize a solution range
5. Follow the numerical clues step-by-step
6. Consider unconventional investigative methods
7. Cross-examine your calculations
8. Ponder what the solution reveals about the mystery

Present your findings as ##<your answer (arabic numerals)> with no spaces.

Case Study:
Mystery: The Discounted Shirt Conundrum
A store sells shirts for $25 each. If they offer a 20% discount on purchases of 3 or more shirts, how much would 5 shirts cost?

Solution:
1. Central question: What's the cost of 5 shirts with the discount?
2. Evidence: $25 per shirt, 20% discount for 3+ shirts, buying 5 shirts
3. Mental image: Five shirts with price tags, a "20% off" sign nearby
4. Hypothesis: Cost will be less than $125 (5 * $25) due to discount
5. Following the clues:
   a) Regular price: 5 * $25 = $125
   b) Discount amount: 20% of $125 = 0.2 * $125 = $25
   c) Discounted price: $125 - $25 = $100
6. Unconventional method: Calculate per-shirt discounted price
   a) Discounted price per shirt: $25 - (20% of $25) = $25 - $5 = $20
   b) Total for 5 shirts: 5 * $20 = $100
7. Cross-examination: Both methods yield $100
8. Revelation: The discount effectively reduces each shirt's price by $5

##100""",
"""Solve this maths word problem:
{content}

Steps:
1. Identify the main question and list given facts.
2. Make an initial estimate of the answer.
3. Develop a mathematically sound plan to solve the problem.
4. Solve step-by-step, using appropriate mathematical operators (addition, subtraction, multiplication, division).
5. Double-check all calculations and reasoning.

Output your answer as ##<your answer (arabic numerals)> with no spaces.

Example:
Problem: John has 5 apples and gives 2 away. How many left?
Estimate: About 3
Solution: 5 - 2 = 3
Double-check: 3 + 2 = 5 (original amount)
##3""",
"""Solve this maths word problem:
{content}

Follow these steps:
1. Identify the main question and list key information, including units.
2. Estimate the answer using mathematical reasoning.
3. Outline your solution approach, considering multiple methods.
4. Solve step-by-step, using correct math operators and maintaining units.
5. Verify your calculations, compare with your estimate, and justify your solution.
6. Consider any creative or unconventional approaches that might simplify the solution.

Output your answer as ##<number> with no spaces, including units if applicable.

Example:
Problem: John has 5 apples and buys 3 more. How many apples does he have now?
Solution:
1. Question: Total apples John has. Given: 5 initial, 3 bought. Unit: apples.
2. Estimate: 5 + 3 ≈ 8 apples (using simple addition).
3. Approach: Direct addition of quantities.
4. Solution: 5 apples + 3 apples = 8 apples
5. Verified. Matches estimate. Justified by the additive property of equality.
6. Creative approach: Could use set theory, defining sets A={{John's initial apples}} and B={{bought apples}}, then find |A or B| = |A| + |B| = 5 + 3 = 8.
Answer: ##8"""
   ]

# Times: 175.350, 201.005, 178.650
def get_market_prompts():
    return ["""Solve this math problem:
{content}

Show your work clearly. Include key steps and reasoning.

Example 1 (Simple arithmetic):
Problem: A train travels 120 km in 2 hours. What is its average speed?
Work:
1. Speed = Distance ÷ Time
2. Distance = 120 km
3. Time = 2 hours
4. Speed = 120 km ÷ 2 hours = 60 km/h
Answer: ##60

Example 2 (Algebra):
Problem: If 3x + 7 = 22, what is the value of x?
Work:
1. Subtract 7 from both sides: 3x = 15
2. Divide both sides by 3: x = 5
Answer: ##5

Example 3 (Geometry - incomplete, finish it):
Problem: A rectangle has a length of 8 cm and a width of 5 cm. What is its area?
Work:
1. Area of rectangle = length × width
2. Length = 8 cm, Width = 5 cm
3. Area = 8 cm × 5 cm = 40 cm²
Answer: ##40

Example 4 (Percentages):
Problem: A shirt originally priced at $80 is on sale for 25% off. What is the sale price?
Work:
1. Calculate the discount: 25% of $80 = 0.25 × $80 = $20
2. Subtract the discount from the original price: $80 - $20 = $60
Answer: ##60

Now solve the given problem, show your work, and provide the answer in the required format.

Answer: ##<answer in arabic numerals>""",
"""SOLVE:
{content}

INTERACTIVE PROBLEM-SOLVING JOURNEY:
1. Warm-up: What's 7-3? (Solve this first!)
   ##4
   Excellent! Now let's tackle word problems.

2. Problem Evolution:
   a) If 5 pens cost $10, how much does 1 pen cost?
      Solution: $10 / 5 = $2
      ##2
   
   b) If 1 pen costs $2, how many pens can you buy with $7?
      Solution: $7 / $2 = 3.5 pens
      ##3.5
   
   c) You have $7 and pens cost $2 each. After buying as many as possible, 
      what percentage of a pen can you buy with the remainder?
      Solution: 
      Pens bought: 3 (costing $6)
      Remainder: $1
      Percentage of a pen: ($1 / $2) * 100 = 50%
      ##50

ASCII ART PROBLEM-SOLVING:
For mixture problems:
  Solution A  Solution B  Mixture
     30%         70%       40%
      |           |         |
      V           V         V
    [====]     [========] [=====]
     10L         20L       30L

MISTAKE SPOTLIGHT:
Problem: A shirt costs $80. It's on sale for 25% off. What's the sale price?
Incorrect: $80 - 25 = $55 (subtracting percentage as a whole number)
Correct: $80 - ($80 * 0.25) = $80 - $20 = $60
##60

PROBLEM-SOLVING MINDSET:
/* Visualize the problem: Draw if needed */
/* Break complex problems into simpler steps */
/* Always check if your answer makes logical sense */

SOLUTION STEPS:
1. Read and analyze
2. Plan your approach
3. Calculate step-by-step
4. Verify your result
5. Present as: ##<answer>

OUTPUT:
##<your answer (arabic numerals)>""",
"""Solve:

{content}

1. Estimate.
2. Model. Define variables.
3. Solve twice. Show steps.
4. Check units.
5. Verify.
6. List errors, alternatives.
7. Apply to real world.

Answer: ##<number>"""
    ]

# Times: 218.334, 209.674, 273.832
def get_hierarchical_prompts():
    return ["""Solve:
{content}

Show all work.

##<youranswer(arabicnumerals)>""",
"""Solve this maths word problem:
{content}
Output answer: ##<your answer (arabic numerals)> with no spaces.""",
"""You're a Word Problem Wizard. Decipher and solve this math word problem:

{content}

1. Identify the key information and question.
2. Translate the words into a mathematical equation.
3. Solve the equation, showing your work briefly.
4. Interpret the result in the context of the original problem.

Conclude with ##<your answer (arabic numerals)> (no spaces)."""
    ]