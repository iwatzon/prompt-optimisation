
# Times: 196.362, 238.122, 207.773
def get_authoritarian_prompts():
    return ['''You will complete a Python function based on its signature and docstring. Follow these steps, outputting your progress after each step:

```python
{content}
```

Step 1: Implement the basic functionality described in the docstring.

Step 2: Add input validation and error handling for edge cases.

Step 3: Optimize the function for performance where possible.

Step 4: Add inline comments to explain any complex logic.

Step 5: Write at least one unit test or test case for the function.

Step 6: Review your implementation. Ensure it follows PEP 8 guidelines and is clean and readable.

Step 7: Add a brief "commit message" style comment explaining your implementation.

After each step, output your progress as:

```python
<your answer so far>
```

After completing all steps, provide your final implementation as:

```python
<your answer>
```''',
'''Let's implement the following function step by step:
```python
{content}
```

Follow these steps:
1. Analyze the function signature and docstring. Explain your understanding.
2. Outline a high-level approach for the implementation.
3. Implement the function body, showing your work incrementally.
4. Refine the implementation, considering edge cases and optimizations.
5. Add inline comments and finalize the function.

After each step, output your progress as:
```python
# Step X:
<your work for this step>
```

For the final output, provide the complete function as:
```python
<your answer>
```''',
'''As an experienced Python Developer working on a data processing pipeline, your task is to implement the following function:

```python
{content}
```

Follow these steps to complete the implementation:

1. Analyze the function signature and docstring carefully.
2. Identify the key components and operations required.
3. Plan your approach, considering potential edge cases and efficiency.
4. Implement the function step by step:
   a. Set up any necessary variables or data structures.
   b. Implement the core logic of the function.
   c. Handle potential edge cases.
   d. Optimize for efficiency where possible.
5. Review your implementation to ensure it follows the docstring specifications and Python best practices.

Here are two examples demonstrating this process:

Example 1 (Simple):
Input:
```python
def square_list(numbers: List[int]) -> List[int]:
    """
    Square each number in the input list.
    
    Args:
    numbers (List[int]): A list of integers
    
    Returns:
    List[int]: A new list with each number squared
    """
```

Output:
```python
def square_list(numbers: List[int]) -> List[int]:
    """
    Square each number in the input list.
    
    Args:
    numbers (List[int]): A list of integers
    
    Returns:
    List[int]: A new list with each number squared
    """
    return [num ** 2 for num in numbers]

Explanation:
I used a list comprehension for efficiency. This approach squares each number in a single line of code, creating a new list without modifying the original. It handles the edge case of an empty list automatically.
```

Example 2 (More complex):
Input:
```python
def process_data(data: List[Dict[str, Union[int, str]]]) -> Dict[str, List[int]]:
    """
    Process a list of dictionaries, grouping numeric values by string keys.
    
    Args:
    data (List[Dict[str, Union[int, str]]]): A list of dictionaries with string keys and int or str values
    
    Returns:
    Dict[str, List[int]]: A dictionary with string keys and lists of integers as values
    """
```

Output:
```python
from collections import defaultdict

def process_data(data: List[Dict[str, Union[int, str]]]) -> Dict[str, List[int]]:
    """
    Process a list of dictionaries, grouping numeric values by string keys.
    
    Args:
    data (List[Dict[str, Union[int, str]]]): A list of dictionaries with string keys and int or str values
    
    Returns:
    Dict[str, List[int]]: A dictionary with string keys and lists of integers as values
    """
    result = defaultdict(list)
    for item in data:
        for key, value in item.items():
            if isinstance(value, int):
                result[key].append(value)
    return dict(result)

Explanation:
I used a defaultdict to efficiently group values. The function iterates through each dictionary in the input list, checking if values are integers before adding them to the result. This handles edge cases like missing keys or non-integer values. The final conversion to a regular dict ensures the return type matches the docstring.
```

Now, implement the given function following this pattern. Output your answer as:

```python
<your answer>
```

After your implementation, briefly explain your approach and any key decisions you made.'''
    ]

# Times: 189.626, 246.207, 227.465
def get_market_prompts():
    return ['''Complete this function:

```python
{content}
```

Match the docstring. Use efficient code. Handle errors if needed. Add brief comments only when necessary.

Output your answer as:
```python
<your answer>
```''',
'''Your mission is to complete the given function based on its signature and docstring. Follow these micro-tasks:

1. Function Analysis:
   a) Decode the function signature.
   b) Unravel the docstring mysteries.
   c) Craft a list of key requirements.

2. Logic Visualization:
   Sketch a simple ASCII flowchart representing the function's logic.

3. Implementation Blueprint:
   a) Identify essential variables.
   b) Map out the main algorithmic steps.
   c) Anticipate and list potential edge cases.

4. Code Crafting:
   a) Build the function incrementally, step-by-step.
   b) Sprinkle enlightening comments throughout.
   c) Ensure your code speaks fluent Pythonic.

5. Self-Reflection Mirror:
   a) Cross-check against the initial requirements.
   b) Verify the handling of sneaky edge cases.
   c) Judge your code's readability and efficiency.

6. Rubber Duck Debugging:
   Explain your implementation to an imaginary junior developer named "Quackers".

7. Polish and Perfect:
   Refine your code based on insights from steps 5 and 6.

Now, complete this function:

{content}

Present your polished function implementation in this format:

```python
<your answer>
```''',
'''Complete this function:

```python
{content}
```

Implement it. Handle edge cases. Apply best practices.

Your answer:

```python
<your answer>
```

Explain key design choices.'''
    ]

# Times: 211.274, 275.883, 311.072
def get_hierarchical_prompts():
    return ['''Complete the following function based on its signature and docstring:
```python
{content}
```
Please output your answer at the end as ```python
<your answer>
```''',
'''You are a Python Function Implementer. Your task:

Analyze and complete this function:

```python
{content}
```

Follow these steps:
1. Study the function signature and docstring carefully.
2. Implement the function body to match the signature exactly.
3. Ensure your code fulfills all docstring requirements.
4. Handle potential edge cases and errors.
5. Optimize for efficiency and readability.

Provide your implementation as:

```python
<your answer>
```''',
'''Complete the following function based on its signature and docstring: 
```python
{content}
```
Please output your answer at the end as ```python
<your answer>
```'''
    ]