
# Times: 14.339, 15.608, 56.956
def get_authoritarian_prompts():
    return [
"""Solve the following maths word problem: {content}

Before solving the problem, make an initial estimate of the answer. Then, use mathematical operators (addition, subtraction, multiplication, division) correctly to solve the problem, and double-check your calculations. Finally, output your answer at the end as ##<your answer (arabic numerals)>.

Your task is to think creatively and explore unconventional approaches to solve the problem, such as breaking it down into smaller steps, visualizing the problem, or considering real-world analogies.""",
"""Solve the following maths word problem: {content}

Before solving the problem, make an initial estimate of the answer. Then, use mathematical operators (addition, subtraction, multiplication, division) correctly to solve the problem, and double-check your calculations. Finally, output your answer at the end as ##<your answer (arabic numerals)>.

Your task is to think creatively and explore unconventional approaches to solve the problem, such as breaking it down into smaller steps, visualizing the problem, or considering real-world analogies.""",
"""As an experienced Mathematician, I would like you to solve the following math word problem:

{content}

First, reframe the problem statement in your own words to identify any underlying assumptions or constraints. Then, consider visualizing the problem in multiple ways, such as through diagrams, graphs, or tables, as this can often lead to novel insights.

Explore related or analogous problems, and challenge any constraints or limitations within the problem statement. Consider the problem from multiple perspectives, such as by imagining yourself as one of the entities or objects involved.

Think beyond the typical "textbook" solutions and consider more creative, out-of-the-box ideas. Explore the use of mathematical concepts or techniques that may not be immediately obvious, and consider how the problem could be solved using unconventional or unexpected methods.

Finally, experiment with alternative problem formulations or representations that may lead to more creative solutions, even if they initially seem unrelated to the original problem. Output your answer at the end as ##<your answer (arabic numerals)>."""
    ]

# Times: 68.566, 83.212, 74.046
def get_market_prompts():
    return ["""
Solve the following mathematics word problem, which has real-world implications for a small business owner:

{content}

To solve this problem, please follow these steps:

1. Carefully read and understand the word problem in the context of a small business owner making a critical financial decision. Identify any unclear parts of the problem and ask clarifying questions to ensure you have a comprehensive understanding of the problem and its relevance to the small business owner's decision-making process.

2. Identify the key information and variables given in the problem. Explain your understanding of the problem and the identified variables, and how they relate to the small business owner's decision-making process.

Example:
The key information and variables given in the problem are:
- The small business owner is considering whether to purchase a new piece of equipment for their manufacturing process.
- The cost of the equipment is $50,000.
- The equipment is expected to increase the business's annual revenue by $20,000 and reduce annual operating costs by $10,000.
- The small business owner has a target return on investment (ROI) of at least 20% over a 5-year period.

The variables in this problem are the cost of the equipment, the expected increase in annual revenue, the expected reduction in annual operating costs, and the target ROI. These factors are all relevant to the small business owner's decision-making process, as they will determine the financial viability and potential return on the investment.

3. Determine the appropriate mathematical operations and calculations needed to solve the problem. Provide a step-by-step explanation of your problem-solving approach, considering potential pitfalls or limitations in your initial solution and exploring alternative approaches that could further optimize the outcome for the small business owner.

4. Show your work and provide the final answer.

5. Validate your answer by checking if it satisfies the given conditions or constraints in the word problem, aligns with the small business owner's financial goals, and considers potential risks or limitations in the solution. Explain how you verified the correctness and relevance of your solution.

6. Output the final answer in the format: ##<your answer (arabic numerals)>

After each step, please confirm your understanding with me before proceeding to the next step. I will provide feedback and guidance as needed to ensure you are on the right track.

This interactive approach is designed to help you understand the problem-solving process, develop critical thinking skills, and reinforce the principles of incremental prompting. By explaining your reasoning and thought process at each step, and considering the practical implications for the small business owner, you will gain a deeper understanding of the problem and enhance your problem-solving abilities.

If applicable, you may also be asked to create a visual representation, such as a graph or diagram, to better understand the relationships between the variables and support the small business owner's decision-making.""",
"""Greetings, esteemed Mathematician! 🧠 I present you with a captivating math word problem that requires your expertise: {content}

Example: 
A farmer has 150 sheep. Each sheep produces 1.2 kilograms of wool per shearing, and the farmer shears the sheep 3 times a year. The farmer sells the wool for $5 per kilogram. How much money will the farmer make from selling the wool in 1 year?

As an experienced Mathematician, let's approach this step-by-step:

**Understanding the Problem**
The key information provided is the number of sheep (150), the amount of wool produced per sheep per shearing (1.2 kilograms), the number of shearings per year (3), and the selling price per kilogram of wool ($5).

**Initial Estimate**
If each sheep produces 1.2 kilograms of wool per shearing, and there are 150 sheep, the total wool produced per shearing is 150 x 1.2 = 180 kilograms. With 3 shearings per year, the total wool produced in 1 year would be 180 x 3 = 540 kilograms. At $5 per kilogram, the estimated total earnings would be around $2,700.

**Solving the Problem**
1. Total wool produced per sheep per year = 1.2 kilograms x 3 shearings = 3.6 kilograms
2. Total wool produced in 1 year = 150 sheep x 3.6 kilograms/sheep = 540 kilograms
3. Total earnings = 540 kilograms x $5 per kilogram = $2,700

**Double-Checking Calculations**
To ensure the accuracy of the solution, I will double-check the calculations.

**Alternative Approach**
As an alternative approach, we can use the formula:
Total earnings = Number of sheep x Wool production per sheep per year x Selling price per kilogram
Plugging in the values, we get:
Total earnings = 150 x 3.6 x $5 = $2,700

The results from both the step-by-step approach and the alternative formula-based approach match, confirming the final answer.

Therefore, the final answer is:

##2700""",
"""As an experienced Word_Problem_Solver, please solve the following math word problem:

{content}

Solve the problem by following these key steps:

1. Identify the type of problem (e.g., percentage, area, revenue) and select an appropriate problem-solving strategy.
2. Thoroughly read and comprehend the problem statements, taking note of the given information and unknown facts.
3. Explore at least three different approaches to solve each problem, discussing the strengths and limitations of each approach.
4. Provide a recommendation for the "best" approach, based on your analysis.
5. Show your work and explain your reasoning step-by-step.
6. Present your solutions in the required format: ##<your answer (arabic numerals)>."""
    ]

# Times: 1.025, 1.335, 1.451
def get_hierarchical_prompts():
    return ["""Solve the following maths word problem: 
{content}
Please output your answer at the end as ##<your answer (arabic numerals)>""",
"""Solve the following maths word problem: 
{content}
Please output your answer at the end as ##<your answer (arabic numerals)>""",
"""Solve the following maths word problem: 
{content}
Please output your answer at the end as ##<your answer (arabic numerals)>""",
    ]
