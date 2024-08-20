class HumanEvalPrompts():
    
    def __init__(self):
        pass
    
    # Max time:  194.12198781967163
    # Min time:  51.18845081329346
    # Average time:  117.11569755077362
    def get_authoritarian_prompts_0(self):
        return [
'''```python
# Task: Complete the following Python function based on its signature and docstring.
# The content will include the function signature and a brief description of its purpose.
# Consider edge cases and constraints.

{content}

# Output your answer at the end as:
```python
<your answer>
```

# Example outputs:
# ```python
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# ```

# ```python
# def fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# ```

# ```python
# def sum_list(lst):
#     if not lst:
#         return 0
#     else:
#         return lst[0] + sum_list(lst[1:])
# ```

# Consider:
# - Input validation (e.g., negative numbers, non-integer inputs)
# - Performance for large inputs
# - Special cases (e.g., empty lists, zero input)
```''',
'''``python
# Task: Complete the function based on the provided signature and docstring in {content}.
# Output the completed function as a Python code block.

# Example 1 (Simple):
# Input:
# def add(a: int, b: int) -> int:
#     """
#     Adds two integers.
#     """
# Output:
# def add(a: int, b: int) -> int:
#     """
#     Adds two integers.
#     """
#     return a + b

# Example 2 (Complex):
# Input:
# def factorial(n: int) -> int:
#     """
#     Returns the factorial of a given number.
#     """
# Output:
# def factorial(n: int) -> int:
#     """
#     Returns the factorial of a given number.
#     """
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

{content}

# Output the function as a Python code block
```python
<your answer>
```
```''',
'''```python
# Task: Complete the following Python function based on its signature and docstring.
# The function should perform the task described in the docstring.
# Please output your answer at the end in the following format:

# ```python
# <your answer>
# ```

# Example 1: Simple Function
# Function Signature: def add(a, b):
# Docstring: """Returns the sum of a and b."""
# Implementation:
# def add(a, b):
#     """Returns the sum of a and b."""
#     return a + b

# Example 2: More Complex Function
# Function Signature: def factorial(n):
# Docstring: """Returns the factorial of n."""
# Implementation:
# def factorial(n):
#     """Returns the factorial of n."""
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

{content}
```''',
'''```python
# Task: Complete the function based on the provided signature and docstring.
# The function signature and docstring will be placed in {content}.
# Output your answer at the end as:
# ```python
# <your answer>
# ```

# Example 1: Simple Function
# Signature and docstring:
# def add(a, b):
#     """
#     Adds two numbers and returns the result.
#     """
# Completed function:
# def add(a, b):
#     """
#     Adds two numbers and returns the result.
#     """
#     return a + b

# Example 2: More Complex Function
# Signature and docstring:
# def factorial(n):
#     """
#     Calculates the factorial of a given number.
#     """
# Completed function:
# def factorial(n):
#     """
#     Calculates the factorial of a given number.
#     """
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

{content}
```''',
'''```python
# Task: Complete the function using the provided signature and docstring.
# Ensure the function follows proper Python syntax.
# Output your answer in the following format:

```python
<your answer>
```

# Example 1: Simple Function
# Signature: def add(a: int, b: int) -> int:
# Docstring: """Returns the sum of a and b."""
# Expected Output:
```python
def add(a: int, b: int) -> int:
    """Returns the sum of a and b."""
    return a + b
```

# Example 2: More Complex Function
# Signature: def factorial(n: int) -> int:
# Docstring: """Returns the factorial of n."""
# Expected Output:
```python
def factorial(n: int) -> int:
    """Returns the factorial of n."""
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
```

{content}
```''',
'''```python
# Task: Complete the function based on the provided signature and docstring in {content}.
# Ensure the function follows standard Python conventions and best practices.
# If the signature or docstring is incomplete or ambiguous, make reasonable assumptions and document them in comments.
# Output your answer as:
```python
<your answer>
```

{content}
```''',
'''```python
# Complete the function using the provided signature and docstring.
# Output your answer as ```python
<your answer>
```

# Example 1:
"""
def add(a: int, b: int) -> int:
    """
    Adds two integers and returns the result.
    """
"""

# Expected output:
```python
def add(a: int, b: int) -> int:
    return a + b
```

# Example 2:
"""
def factorial(n: int) -> int:
    """
    Computes the factorial of a non-negative integer.
    """
"""

# Expected output:
```python
def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
```

{content}
```''',
'''```python
# Task: Complete the Python function provided in {content}.
# Ensure the function follows standard Python conventions.
# Output the complete function in the following format:

# ```python
# <your answer>
# ```

{content}
```''',
'''```python
# Task: Implement the function provided in {content} based on its signature and docstring.
# Context: {content} contains the function signature and docstring. Implement the function as specified.
# Instructions: Ensure the function handles all edge cases and follows best practices.
# Examples:
# Example 1:
# {content}:
# def example_function(param1, param2):
#     """
#     This function takes two parameters and returns their sum.
#     Args:
#         param1 (int): The first parameter.
#         param2 (int): The second parameter.
#     Returns:
#         int: The sum of param1 and param2.
#     """
#     # Your implementation here
# Output:
# ```python
# def example_function(param1, param2):
#     return param1 + param2
# ```

# Example 2:
# {content}:
# def complex_function(param1, param2, param3):
#     """
#     This function takes three parameters and returns a complex calculation.
#     Args:
#         param1 (int): The first parameter.
#         param2 (int): The second parameter.
#         param3 (int): The third parameter.
#     Returns:
#         int: The result of the complex calculation.
#     """
#     # Your implementation here
# Output:
# ```python
# def complex_function(param1, param2, param3):
#     return (param1 * param2) + param3
# ```

# Example 3:
# {content}:
# def edge_case_function(param1):
#     """
#     This function takes one parameter and returns a specific value for edge cases.
#     Args:
#         param1 (int): The parameter.
#     Returns:
#         int: The result based on edge cases.
#     """
#     # Your implementation here
# Output:
# ```python
# def edge_case_function(param1):
#     if param1 == 0:
#         return 0
#     elif param1 < 0:
#         return -1
#     else:
#         return 1
# ```

# Complete the function in {content} and output your answer as:
```python
<your answer>
```
```''',
'''```python
# Complete the following Python function based on its signature and docstring.
# Examples:
# Incomplete:
# def add(a, b):
#     """
#     Adds two numbers and returns the result.
#     """
#     # Your code here
# Completed:
# def add(a, b):
#     """
#     Adds two numbers and returns the result.
#     """
#     return a + b

# Incomplete:
# def factorial(n):
#     '"""'
#     Returns the factorial of a given number.
#     """
#     # Your code here
# Completed:
# def factorial(n):
#     """
#     Returns the factorial of a given number.
#     """
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

{content}

```python
<your answer>
```
```'''
        ]

    # Max time:  141.20320796966553
    # Min time:  29.287969827651978
    # Average time:  83.71572244167328
    def get_authoritarian_prompts_1(self):
        return [
'''```python
# Below is a Python function signature and its docstring (a description of what the function does):
{content}

# Your task is to:
# 1. Implement the function based on the given signature and docstring.
# 2. Ensure the implementation follows the provided description and requirements.

# Example format for the completed function:
# ```python
# def example_function(param1: int, param2: str) -> bool:
#     """
#     This function checks if the integer is positive and the string is non-empty.
#     """
#     return param1 > 0 and bool(param2)

# Output the completed function code in the same format as the example:
```python
<your answer>
```
```''', 
'''```python
# Provide a Python function signature and docstring within the `{content}` placeholder.
# Your task is to complete the function based on its signature and docstring.

{content}

# Your answer should be in the following format:
```python
<your answer>
```

# Example 1 (Simple):
# Input:
"""
def add(a, b):
    \"\"\"Adds two numbers\"\"\"
    pass
"""

# Output:
```python
def add(a, b):
    \"\"\"Adds two numbers\"\"\"
    return a + b
```

# Example 2 (Moderate):
# Input:
"""
def factorial(n):
    \"\"\"Returns the factorial of a number\"\"\"
    pass
"""

# Output:
```python
def factorial(n):
    \"\"\"Returns the factorial of a number\"\"\"
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

# Example 3 (Complex with Error Handling):
# Input:
"""
def divide(a, b):
    \"\"\"Divides a by b, raising an error if b is zero\"\"\"
    pass
"""

# Output:
```python
def divide(a, b):
    \"\"\"Divides a by b, raising an error if b is zero\"\"\"
    if b == 0:
        raise ValueError("The divisor 'b' cannot be zero.")
    return a / b
```
```''',
'''Please complete the function based on the signature and docstring provided in _{content}_. Ensure the final output is within the following markers:

```python
<your answer>
```

### Example:
If `{content}` contains:
```python
def find_max(numbers):
    """
    Returns the maximum number from a list of numbers.
    """
```
Your output should be:
```python
def find_max(numbers):
    """
    Returns the maximum number from a list of numbers.
    """
    if not numbers:
        return None
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number
```
```''',
'''```python
# Task: Implement the function based on its signature and docstring provided below.
# The content placeholder will include the function signature and docstring for implementation.

{content}

# Example of a function signature and its implementation:
# Signature:
# def add(a, b):
# Docstring:
# """
#     Adds two numbers.
#     Args:
#         a (int): The first number.
#         b (int): The second number.
#     Returns:
#         int: The sum of the two numbers.
# """
# Expected implementation:
# def add(a, b):
#     """
#     Adds two numbers.
#     Args:
#         a (int): The first number.
#         b (int): The second number.
#     Returns:
#         int: The sum of the two numbers.
#     """
#     # Following best practices, writing clean and maintainable code.
#     return a + b

# Ensure your output is formatted exactly like this:
```python
<your answer>
```
```

# Notes:
# - Follow best practices in software engineering (e.g., PEP 8).
# - Write clean, maintainable, and well-documented code.
# - Consider the performance implications of your code.
```''',
'''Complete the given Python function based on its signature and docstring.

**Instructions:**
1. **Implement the Function Body**:
   - Write logic to perform the task described in the docstring.
   - Ensure your implementation is efficient in terms of time and space complexity.

2. **Document Your Code**:
   - Add a docstring explaining what the function does, its parameters, and its return value.
   - Include inline comments to explain any complex steps in your implementation.

Write your solution in a Python code block like this:

```python
{content}
# Your implementation here
```

**Examples**:
1. **Simple String Reversal**:
    ```python
    def reverse_string(s: str) -> str:
        """
        Reverses the given string.
        
        :param s: The string to be reversed.
        :return: The reversed string.
        """
        # Use Python slicing to reverse the string efficiently.
        return s[::-1]

    # Example usage:
    # reversed_string = reverse_string("hello")
    # print(reversed_string)  # Output: "olleh"
    ```

2. **Removing Duplicates from a List**:
    ```python
    def remove_duplicates(lst: list) -> list:
        """
        Removes duplicates from the list while maintaining order.
        
        :param lst: The list from which to remove duplicates.
        :return: A list with duplicates removed.
        """
        seen = set()
        result = []
        for x in lst:
            # Check if the element is already in the set of seen elements
            if x not in seen:
                result.append(x)
                seen.add(x)  # Add the element to the seen set
        return result

    # Example usage:
    # unique_list = remove_duplicates([1, 2, 2, 3, 4, 4])
    # print(unique_list)  # Output: [1, 2, 3, 4]
    ```

**Output your answer at the end as:**
```python
<your answer>
```''',
'''```python
Complete the Python function provided in the placeholder {content} based on its signature and docstring.

Output the completed function in this format:
```python
<your answer>
```.

For example, if `{content}` is:

```python
def greet(name):
    """Return a greeting message including the given name."""
```

The expected output is:
```python
def greet(name):
    """Return a greeting message including the given name."""
    return f"Hello, {{name}}!"
```

If `{content}` is:

```python
def add(a, b):
    """Return the sum of two numbers."""
```

The expected output is:
```python
def add(a, b):
    """Return the sum of two numbers."""
    return a + b
```

If `{content}` is:

```python
def filter_even(numbers):
    """Return a list of even numbers from the provided list."""
```

The expected output is:
```python
def filter_even(numbers):
    """Return a list of even numbers from the provided list."""
    return [num for num in numbers if num % 2 == 0]
```

Please note:
1. Complete the function using the provided signature and docstring.
2. Ensure the output strictly follows the specified format.
```''',
'''```plaintext
Complete the function using the given signature and docstring:

Signature and Docstring:
{content}

Output your answer in this format:
```python
<your answer>
```
```''',
'''```python
# Task: Complete the function below based on its signature and docstring.
# Follow best practices: clear documentation, meaningful variable names, and performance considerations.

# Function Signature and Docstring:
{content}

# Example:
# For a factorial function:
# Input: 5
# Output: 120

# Provide your solution:
```python
<your answer>
```
```''',
'''```python
"""
{content}
"""

Complete the function in `content` using its signature and docstring.

Examples:

Simple Function:
```python
def add(a, b):
    """
    Add two numbers and return the result.
    """
    return a + b
```

Complex Function:
```python
def factorial(n):
    """
    Compute the factorial of a non-negative integer n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
```

If docstring or signature is incomplete, output:
```python
"Incomplete docstring or signature."
```

Output the completed function or error message as follows:
```python
<your answer>
```
```''',
'''```python
# Your task is to define a function for sorting a list of integers.
# Sorting is a fundamental operation in programming and is used in various scenarios such as organizing data for efficient search and analysis.
#
# Insert a Python code snippet within {content} that defines the following function:
"""
def sort_list(input_list):
    """
    Takes a list of integers and returns the list sorted in ascending order.
    """
"""
# Provide a sample function call and the expected output.
# Format your examples as shown below:
# sorted_list = sort_list([3, 1, 2])
# Expected Output: [1, 2, 3]

# Output your answer at the end as:
```python
<your answer>
```
```'''
        ]

    
    def get_market_prompts_0(self):
        return [
'''```python
Complete the function based on its signature and docstring below:

{content}

Instructions:
1. Review the function signature and docstring for errors or inefficiencies.
2. Ensure the function handles a wide range of inputs, including edge cases.
3. Consider the scalability and maintainability of the function. Think about potential performance bottlenecks and how the function might be extended or modified in the future.
4. Consider the trade-offs of different implementation approaches and choose the most optimal solution for the given context.
5. Ensure the function is well-documented, including clear and comprehensive docstrings and inline comments where necessary.
6. Provide constructive feedback on the function signature and docstring.

Example:
```python
def add(a: int, b: int) -> int:
    """
    Adds two integers together.
    
    Args:
    a (int): The first integer.
    b (int): The second integer.
    
    Returns:
    int: The sum of the two integers.
    """
    return a + b

# Feedback:
# The function signature and docstring are clear and efficient. However, consider adding type checks to ensure the inputs are integers.
```

Output your answer as:
```python
<your answer>
```
```''',
'''```python
{content}
```
Complete the function based on its signature and docstring. Ensure the code follows best practices:
- Write clean, readable, and maintainable code
- Handle edge cases and include error handling
- Consider performance implications

### Examples

#### Simple Example
```python
def add(a, b):
    """
    Add two numbers and return the result.
    """
    return a + b
```
Output:
```python
def add(a, b):
    """
    Add two numbers and return the result.
    """
    return a + b
```

#### Intermediate Example
```python
def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
```
Output:
```python
def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
```

#### Complex Example
```python
def find_max_subarray(arr):
    """
    Find the contiguous subarray within a one-dimensional array of numbers which has the largest sum.
    """
    max_sum = float('-inf')
    current_sum = 0
    for num in arr:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
```
Output:
```python
def find_max_subarray(arr):
    """
    Find the contiguous subarray within a one-dimensional array of numbers which has the largest sum.
    """
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    max_sum = float('-inf')
    current_sum = 0
    for num in arr:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
```

**Output your answer at the end as**:
```python
<your answer>
```
''',
'''```python
{content}
```
Please complete the function based on its signature and docstring. Ensure the following:
- The code is scalable and maintainable.
- Document architectural decisions.
- Review for errors and inefficiencies.
- Implement error handling.
- Consider performance implications.
- Think about testing, including unit tests and edge cases.
- Ensure readability and documentation.

Output your answer at the end as ```python
<your answer>
```

### Examples:

#### Simple Example:
```python
def add(a, b):
    """
    Adds two numbers.
    
    Args:
    a (int): The first number.
    b (int): The second number.
    
    Returns:
    int: The sum of the two numbers.
    """
    return a + b

# Example usage:
# add(2, 3) -> 5
```

#### Complex Example:
```python
def process_data(data):
    """
    Processes a list of data and returns the processed result.
    
    Args:
    data (list): A list of data points.
    
    Returns:
    dict: A dictionary with processed data.
    """
    if not isinstance(data, list):
        raise ValueError("Input must be a list")
    
    processed = {{}}
    for item in data:
        if not isinstance(item, int):
            continue
        if item in processed:
            processed[item] += 1
        else:
            processed[item] = 1
    
    return processed

# Example usage:
# process_data([1, 2, 2, 3, 3, 3]) -> {{1: 1, 2: 2, 3: 3}}
```

### Explanation of Examples:
- **Simple Example**: Demonstrates a basic function with a clear docstring and simple logic.
- **Complex Example**: Shows error handling, type checking, and a more complex processing logic.

By following these examples, you can ensure your function is well-documented, efficient, and handles errors appropriately.''',
'''```python
Complete the following function based on its signature and docstring. Ensure the function is efficient, handles edge cases, and includes comments or explanations to clarify your reasoning:

{content}

Please output your answer at the end as ```python
<your answer>
```
```''',
'''```python
Complete the function based on its signature and docstring. Ensure the code is clean, maintainable, and efficient. Check for errors, inefficiencies, and edge cases. Comment on potential improvements, including performance considerations.

Examples:

1. Simple:
```python
def add(a: int, b: int) -> int:
    """
    Adds two integers together.
    """
    # Your implementation here

# Expected output:
# def add(a: int, b: int) -> int:
#     """
#     Adds two integers together.
#     """
#     return a + b
#
# Comments:
# - Simple and efficient.
# - No errors or edge cases.
```

2. Moderate:
```python
def find_max(numbers: list) -> int:
    """
    Finds the maximum number in a list.
    """
    # Your implementation here

# Expected output:
# def find_max(numbers: list) -> int:
#     """
#     Finds the maximum number in a list.
#     """
#     if not numbers:
#         raise ValueError("The list is empty")
#     return max(numbers)
#
# Comments:
# - Added error handling for empty list.
# - Used built-in max function.
```

3. Complex:
```python
def fibonacci(n: int) -> int:
    """
    Returns the nth Fibonacci number.
    """
    # Your implementation here

# Expected output:
# def fibonacci(n: int) -> int:
#     """
#     Returns the nth Fibonacci number.
#     """
#     if n <= 0:
#         raise ValueError("n must be a positive integer")
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     a, b = 0, 1
#     for _ in range(2, n):
#         a, b = b, a + b
#     return b
#
# Comments:
# - Added error handling for non-positive integers.
# - Used an iterative approach.
```

4. Performance Consideration:
```python
def sum_large_list(numbers: list) -> int:
    """
    Sums a large list of numbers.
    """
    # Your implementation here

# Expected output:
# def sum_large_list(numbers: list) -> int:
#     """
#     Sums a large list of numbers.
#     """
#     if not numbers:
#         return 0
#     return sum(numbers)
#
# Comments:
# - Used built-in sum function for efficiency.
# - Considered the case of an empty list.
```

Now, complete the following function based on its signature and docstring. Ensure the code is clean, maintainable, and efficient. Check for errors, inefficiencies, and edge cases. Comment on potential improvements, including performance considerations:

{content}

Output your answer at the end as ```python
<your answer>
```
```''',
'''```python
{content}
```
Complete the function based on its signature and docstring. Follow these steps:

1. **Error Handling:**
   - Identify potential errors that could occur.
   - Implement appropriate error handling mechanisms (e.g., raising exceptions).

2. **Input Validation:**
   - Validate the inputs to ensure they meet the expected criteria.
   - Raise appropriate errors if the inputs are invalid.

3. **Clean and Maintainable Code:**
   - Use meaningful variable names.
   - Write clear and concise code.
   - Add comments where necessary to explain complex logic.

4. **Performance Considerations:**
   - Optimize the code for performance where possible.
   - Avoid unnecessary computations or memory usage.

### Examples:

1. **Simple Example:**
```python
def add(a: int, b: int) -> int:
    """
    Adds two integers together.

    :param a: First integer
    :param b: Second integer
    :return: Sum of a and b
    """
    return a + b
```

2. **Example with Error Handling:**
```python
def divide(a: float, b: float) -> float:
    """
    Divides one number by another.

    :param a: Numerator
    :param b: Denominator
    :return: Result of division
    :raises ValueError: If b is zero
    """
    if b == 0:
        raise ValueError("Denominator cannot be zero.")
    return a / b
```

3. **Example with Input Validation:**
```python
def find_max(numbers: list) -> int:
    """
    Finds the maximum number in a list.

    :param numbers: List of integers
    :return: The maximum integer in the list
    :raises ValueError: If the list is empty
    """
    if not numbers:
        raise ValueError("The list cannot be empty.")
    return max(numbers)
```

Output your answer at the end as ```python
<your answer>
```''',
'''```python
"""
Implement the function using its signature and docstring in the {content} placeholder.
Ensure the code is modular, readable, and efficient. Use comments to explain your approach.

Follow these steps:

1. **Understand the Function Signature and Docstring:**
   - Read the function signature and docstring carefully to understand the purpose of the function, its parameters, and its return value.

2. **Plan the Implementation:**
   - Identify the main tasks that the function needs to perform.
   - Consider any edge cases or potential errors that need to be handled.

3. **Write the Code:**
   - Implement the function in a modular and readable manner.
   - Use comments to explain your approach and any important decisions.

Examples:

1. Simple Addition:
```python
def add(a, b):
    """
    Adds two numbers together.
    
    Parameters:
    a (int): The first number.
    b (int): The second number.
    
    Returns:
    int: The sum of the two numbers.
    """
    # Return the sum of a and b
    return a + b
```

2. Factorial Calculation:
```python
def factorial(n):
    """
    Calculates the factorial of a number.
    
    Parameters:
    n (int): The number to calculate the factorial of.
    
    Returns:
    int: The factorial of the number.
    """
    # Use recursion to calculate the factorial
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

3. Handling Edge Cases and Errors:
```python
def divide(a, b):
    """
    Divides one number by another.
    
    Parameters:
    a (int): The numerator.
    b (int): The denominator.
    
    Returns:
    float: The result of the division.
    
    Raises:
    ValueError: If the denominator is zero.
    """
    # Check for division by zero
    if b == 0:
        raise ValueError("The denominator cannot be zero.")
    return a / b
```

Output your answer as:
```python
<your answer>
```
"""
{content}
```''',
'''```python
{content}

# Complete the function based on its signature and docstring.
# Ensure the implementation is scalable and maintainable.
# Consider the trade-offs of different approaches and document your decisions.
# Output your answer at the end as ```python <your answer> ```.

# Examples:

# Example 1:
# def add(a: int, b: int) -> int:
# """Returns the sum of a and b."""
# def add(a: int, b: int) -> int:
#     return a + b

# Example 2:
# def greet(name: str) -> str:
# """Returns a greeting message for the given name."""
# def greet(name: str) -> str:
#     return f"Hello, {{name}}!"

# Example 3:
# def factorial(n: int) -> int:
# """Returns the factorial of a non-negative integer n."""
# def factorial(n: int) -> int:
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# Example 4:
# def find_max(numbers: list) -> int:
# """Returns the maximum number in a list of numbers."""
# def find_max(numbers: list) -> int:
#     max_num = numbers[0]
#     for num in numbers:
#         if num > max_num:
#             max_num = num
#     return max_num

# Example 5:
# def reverse_string(s: str) -> str:
# """Returns the reverse of the input string."""
# def reverse_string(s: str) -> str:
#     return s[::-1]

```''',
'''```python
# Complete the function based on its signature and docstring below.
# Consider the following:
# - Scalability: Ensure the function can handle increasing amounts of work or data.
# - Maintainability: Ensure the function is easy to understand, modify, and extend.
# - Trade-offs: Consider different architectural patterns and their trade-offs.
# Document any architectural decisions you make.

{content}

# Examples:

# Example 1: Simple Function
# Signature: def add(a: int, b: int) -> int:
# Docstring: """Returns the sum of a and b."""
# Expected Output:
# ```python
# def add(a: int, b: int) -> int:
#     """
#     Returns the sum of a and b.
#     """
#     return a + b
# ```

# Example 2: Complex Function with Scalability Considerations
# Signature: def process_data(data: List[int]) -> List[int]:
# Docstring: """Processes the input data and returns the processed data."""
# Expected Output:
# ```python
# def process_data(data: List[int]) -> List[int]:
#     """
#     Processes the input data and returns the processed data.
#     """
#     # Using list comprehension for scalability
#     processed_data = [x * 2 for x in data]
#     return processed_data
# ```

# Example 3: Recursive Function
# Signature: def factorial(n: int) -> int:
# Docstring: """Returns the factorial of n."""
# Expected Output:
# ```python
# def factorial(n: int) -> int:
#     """
#     Returns the factorial of n.
#     """
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
# ```

# Example 4: Function with Error Handling
# Signature: def safe_divide(a: int, b: int) -> float:
# Docstring: """Returns the result of dividing a by b. Raises ValueError if b is zero."""
# Expected Output:
# ```python
# def safe_divide(a: int, b: int) -> float:
#     """
#     Returns the result of dividing a by b. Raises ValueError if b is zero.
#     """
#     if b == 0:
#         raise ValueError("Division by zero is not allowed")
#     return a / b
# ```

# Example 5: Function with External Dependency
# Signature: def fetch_data(url: str) -> dict:
# Docstring: """Fetches data from the given URL and returns it as a dictionary."""
# Expected Output:
# ```python
# import requests
# 
# def fetch_data(url: str) -> dict:
#     """
#     Fetches data from the given URL and returns it as a dictionary.
#     """
#     response = requests.get(url)
#     return response.json()
# ```

# Documenting Architectural Decisions:
# - Use comments to explain any architectural decisions made.
# - Example:
# ```python
# def example_function():
#     # Decision: Using list comprehension for better performance and readability.
#     result = [x * 2 for x in range(10)]
#     return result
# ```

# Output your answer at the end as
```python
<your answer>
```
```''',
'''```python
{content}
```
Complete the function based on its signature and docstring. Ensure:
- Best practices.
- Clean, maintainable code.
- Performance considerations.

Steps:
1. Understand the function signature and docstring.
2. Implement the function with best practices, clean code, and performance in mind.

Examples:
1. Simple function:
```python
def add(a: int, b: int) -> int:
    """
    Adds two integers together.

    Args:
    a (int): The first integer.
    b (int): The second integer.

    Returns:
    int: The sum of the two integers.
    """
    return a + b
```
Explanation: Basic arithmetic operation.

2. Intermediate function:
```python
def factorial(n: int) -> int:
    """
    Computes the factorial of a non-negative integer.

    Args:
    n (int): A non-negative integer.

    Returns:
    int: The factorial of the integer.
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)
```
Explanation: Involves recursion and a conditional check.

3. Complex function:
```python
def merge_sort(arr: list) -> list:
    """
    Sorts a list of integers using the merge sort algorithm.

    Args:
    arr (list): A list of integers.

    Returns:
    list: A sorted list of integers.
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left: list, right: list) -> list:
    """
    Merges two sorted lists into one sorted list.

    Args:
    left (list): A sorted list of integers.
    right (list): A sorted list of integers.

    Returns:
    list: A merged and sorted list of integers.
    """
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```
Explanation: Recursive sorting algorithm with a helper function.

Output your answer as:
```python
<your answer>
```'''
        ]
    
    # Max time:  287.6878571510315
    # Min time:  60.9270920753479
    # Average time:  133.7541213274002
    def get_market_prompts_1(self):
        return [
'''```python
Complete the following function based on its signature and docstring:
```python
{content}
```
Ensure that the completed function:
- Is error-free and includes proper error handling (e.g., invalid inputs, type errors)
- Considers edge cases thoroughly
- Is efficient in terms of both time and space complexity
- Follows best practices in software engineering, such as adhering to PEP 8 guidelines
- Is clean and maintainable with meaningful variable names and comments where necessary
- Considers performance implications and avoids common pitfalls (e.g., unnecessary loops, deep recursion)
- Is structured in a way that makes it easy to write unit tests for verification

Please output your answer at the end as ```python
<your answer>```.
```''',
'''```python
Given the following function signature and docstring:

{content}

Follow these steps to complete the function:

1. **Understand and Plan:**
   - Identify the input parameters and the function's purpose from the docstring.
     - Example: If the docstring states the function adds two numbers, identify the inputs as two integers.
   - Consider the usual context in which similar functions are used.

2. **Implement the Function:**
   - Convert your plan into Python code ensuring all requirements and constraints from the docstring are met.
   - Refer to examples based on the type of function you are implementing:
     - **Basic Calculation:** For simple arithmetic operations.
       ```python
       def add_numbers(num1, num2): 
           return num1 + num2
       ```
     - **Conditional Logic:** For decision making based on conditions.
       ```python
       def check_even(num): 
           return num % 2 == 0
       ```
     - **Loops:** For iterating over collections.
       ```python
       def sum_list(lst): 
           total = 0 
           for num in lst: 
               total += num 
           return total
       ```
     - **Multiple Data Types:** For operations involving several data types.
       ```python
       def concat_strings(s1, s2, times): 
           return (s1 + s2) * times
       ```
     - **Complex Logic:** For more intricate calculations or logic.
       ```python
       def fibonacci(n):
           if n <= 0:
               return []
           a, b = 0, 1
           result = [a]
           for _ in range(1, n):
               a, b = b, a + b
               result.append(a)
           return result
       ```

3. **Review for Accuracy:**
   - Verify the function for correctness by testing with various inputs, including edge cases.
     - Example:
       ```python
       print(add_numbers(1, 2))  # Expected: 3
       print(check_even(2))  # Expected: True
       print(sum_list([1, 2, 3]))  # Expected: 6
       print(concat_strings("a", "b", 3))  # Expected: "ababab"
       print(fibonacci(5))  # Expected: [0, 1, 1, 2, 3]
       ```

4. **Output the Completed Function:**
   - Provide the code within a `python` code block as follows:
   - Ensure to maintain proper formatting and indentation.

```python
<your answer>
```
''',
'''```python
"""
Complete the function using its signature and docstring below:

{content}

Follow these guidelines:
- Use clean, maintainable, and well-documented code.
- Use meaningful names and comments.
- Optimize for performance (time and space).
- Consider scalability and maintainability.
- Document architectural decisions and trade-offs.
- Break down larger problems into smaller, manageable functions.
- Design functions that can be reused across different parts of the project.
- Implement error handling to make the function robust.
- Where applicable, document performance benchmarks to illustrate the trade-offs made.

Here are some examples to help you understand how to approach the task:

Example 1:
```python
def add(a: int, b: int) -> int:
    """
    Add two integers and return the result.
    
    :param a: First integer to add.
    :param b: Second integer to add.
    :return: Sum of the two integers.
    """
    # Adding the two integers
    return a + b
```

Explanation: This function takes two integers as input and returns their sum by simply adding them together.

Example 2:
```python
def factorial(n: int) -> int:
    """
    Compute the factorial of a number.
    
    :param n: Non-negative integer.
    :return: Factorial of the number.
    """
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    
    # Recursive case: n! = n * (n-1)!
    return n * factorial(n - 1)
```

Explanation: This function calculates the factorial of a non-negative integer using recursion. The recursive approach is straightforward and clean for understanding, but can be less optimal for large numbers due to potential stack overflow.

Example 3:
```python
def fibonacci(n: int) -> int:
    """
    Generate the n-th Fibonacci number.
    
    :param n: Index of the Fibonacci sequence (0-based).
    :return: The n-th Fibonacci number.
    """
    # Iterative approach for better performance in time and space
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    
    # The nth Fibonacci number
    return a
```

Explanation: This function computes the n-th Fibonacci number using an iterative approach. 
The iterative solution is more efficient in terms of time and space complexity compared to the recursive approach. 
Choosing iterations over recursion is a trade-off that improves performance and avoids potential stack overflow issues with large input values, making it more scalable and maintainable.

Example 4:
```python
def safe_divide(a: int, b: int) -> float:
    """
    Divide two integers and return the result. Raises an error if the divisor is zero.
    
    :param a: The dividend.
    :param b: The divisor.
    :return: The result of the division.
    """
    # Checking for division by zero
    if b == 0:
        raise ValueError("Cannot divide by zero")
    
    # Performing the division
    return a / b
```

Explanation: This function divides two integers and returns the result while handling the division by zero edge case by raising an error. This makes the function more robust and maintainable by ensuring it handles erroneous input gracefully.

Output your answer as:
```python
<your answer>
```
"""
```''',
'''```python
{content}
```

Complete the function based on its signature and docstring. Ensure the function is:
- Scalable: Efficient for large inputs using appropriate algorithms or data structures.
- Maintainable: Easy to understand and modify by future developers.
- Well-documented: Include clear comments, docstrings, and handle edge cases.

### Steps to Follow:
1. **Input Validation**: Start by validating the inputs to ensure they meet the expected criteria.
2. **Identify Sub-Tasks**: Break down the problem into smaller sub-tasks or components if applicable.
3. **Algorithm Efficiency**: Choose data structures and algorithms that ensure the function scales well with large inputs.
4. **Handle Edge Cases**: Identify and handle edge cases to ensure robustness.
5. **Write Docstrings and Comments**: Clearly document the function, including comments that explain non-obvious parts of the code.

### Consider Different Approaches:
- Think of different algorithms and justify your choices with comments explaining the pros and cons of each.
- Decide on the most suitable approach considering efficiency, readability, and maintainability.

Output the completed function as:
```python
<your answer>
```

### Examples:

#### Example 1:
Context:
This function calculates the factorial of a non-negative integer. Factorial can grow very large, and an efficient approach must be chosen to avoid hitting recursion limits in Python.

Function Signature and Docstring:
```python
def factorial_iterative(n):
    """
    Calculate the factorial of a number using an iterative approach.
    
    Args:
    n (int): A non-negative integer whose factorial is to be computed.
    
    Returns:
    int: Factorial of the input number.
    """
```

Completed Function:
```python
def factorial_iterative(n):
    """
    Calculate the factorial of a number using an iterative approach.
    
    Args:
    n (int): A non-negative integer whose factorial is to be computed.
    
    Returns:
    int: Factorial of the input number.
    """
    
    # Validate input
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Initialize result
    result = 1
    
    # Compute factorial iteratively
    for i in range(2, n + 1):
        result *= i
    
    return result
```

Explanation:
- **Scalability**: The iterative approach avoids recursion limits.
- **Maintainability**: Simple loop and clear variable names.
- **Documentation**: Clear docstring, input validation, and comments explaining each step.

#### Example 2:
Context:
This function calculates the sum of squares of a list of integers. Efficient summing operations are crucial for large input lists.

Function Signature and Docstring:
```python
def sum_of_squares(nums):
    """
    Calculate the sum of squares of a list of numbers.
    
    Args:
    nums (list): A list of integers.
    
    Returns:
    int: The sum of the squares of the input list numbers.
    """
```

Completed Function:
```python
def sum_of_squares(nums):
    """
    Calculate the sum of squares of a list of numbers.
    
    Args:
    nums (list): A list of integers.
    
    Returns:
    int: The sum of the squares of the input list numbers.
    """
    
    # Validate input
    if not all(isinstance(num, int) for num in nums):
        raise ValueError("All elements in the list must be integers")
    
    # Calculate sum of squares
    return sum(num ** 2 for num in nums)
```

Explanation:
- **Scalability**: Uses a generator expression within sum for efficiency.
- **Maintainability**: Simple one-liner with clear intent.
- **Documentation**: Clear docstring and inline comment for input validation.

#### Example 3:
Context:
This function finds the longest substring without repeating characters in a given string. Efficient substring processing is critical for long strings and requires careful handling of data structures.

Function Signature and Docstring:
```python
def longest_unique_substring(s):
    """
    Find the longest substring without repeating characters.
    
    Args:
    s (str): The input string.
    
    Returns:
    str: The longest substring without repeating characters.
    """
```

Completed Function:
```python
def longest_unique_substring(s):
    """
    Find the longest substring without repeating characters.
    
    Args:
    s (str): The input string.
    
    Returns:
    str: The longest substring without repeating characters.
    """
    
    # Dictionary to store the last positions of each character
    last_seen = {{}}
    start = 0  # Starting index of current substring without repeating characters
    max_len = 0  # Length of the longest substring found
    max_substr = ""  # The longest substring without repeating characters
    
    for i, char in enumerate(s):
        if char in last_seen and last_seen[char] >= start:
            start = last_seen[char] + 1  # Move start to the right of the last seen duplicate character
        
        last_seen[char] = i
        
        # Update maximum length and substring
        if i - start + 1 > max_len:
            max_len = i - start + 1
            max_substr = s[start:i+1]
    
    return max_substr
```

Explanation:
- **Scalability**: Uses a sliding window technique ensuring a linear time complexity, efficient for long strings.
- **Maintainability**: Clear variable names and concise logic.
- **Documentation**: Detailed comments and clear explanation of the algorithm.

```python
<your answer>
```''',
'''```python
# Complete the function implementation in {content}. Ensure it works correctly, handles edge cases, and is efficient.
# Review for any errors or inefficiencies and fix them.
# Add notes for any complex logic, optimizations, or key considerations.
{content}
# Output your answer as:
```python
<your answer>
```
```''',
'''```python
{content}

# As an experienced software developer, your task is to complete the function based on its given signature and docstring.
# Please consider the following:
# - Ensure that your implementation is scalable, maintainable, and follows best practices.
# - Use comments to explain your design decisions and the rationale behind them.
# - If applicable, include error handling and input validation.
# - Assume the function will be used in a highly concurrent environment (e.g., web server handling multiple requests).
# - Output the final function as follows:
# ```python
# <your answer>
# ```
```''',
'''```python
Complete the following function based on its signature and docstring. Ensure your implementation addresses:

1. **Error Handling**:
   - Handle division by zero.
   - Handle file operations:
     - Check if file exists (`FileNotFoundError`).
     - Ensure proper permissions (`PermissionError`).
     - Use `with` statement to ensure files are closed properly.

2. **Efficiency**:
   - Optimize time and space complexity:
     - Avoid unnecessary computations.
     - Use efficient algorithms, such as caching and parallel processing.

3. **Edge Cases**:
   - Handle scenarios like:
     - Empty lists.
     - Large input strings.

Examples:

```python
def safe_divide(a, b):
    """
    Divides two numbers, a and b, and returns the result.
    Handles the case where b is zero by returning None.
    """
<your answer>

# Expected output
```
```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
```

```python
def read_file_content(filename):
    """
    Reads the content of a file and returns it as a string.
    Handles file not found errors gracefully.
    """
<your answer>

# Expected output
```
```python
def read_file_content(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."
```

{content}

Output your answer at the end as ```python
<your answer>
```
```''',
'''```python
Based on the provided function signature and docstring, your task is to complete the function while adhering to best practices in software engineering. Ensure the code is correct, handles edge cases, and uses meaningful variable names. Treat the docstring as an authoritative guide for the function's expected behavior.

### Steps to complete the task:
1. **Read and understand the function signature and its docstring.** Identify the goals and requirements outlined in the docstring.
2. **Plan your implementation.** Consider necessary logic, potential edge cases, and how to name variables clearly.
3. **Write the function.** Follow your plan, ensuring the code is correct and clear.
4. **Review your implementation.** Verify that all requirements from the docstring are met, and all edge cases are handled.

**Example for context**: Consider the function signature `def add(a, b):` and the docstring "Return the sum of a and b". The function should handle non-integer inputs, large numbers, etc. Here's an example implementation:

```python
def add(a, b):
    # Ensure both inputs are numbers, handle large values
    return a + b
```

Once you've implemented the function, format your output as follows:

```python
<your answer>
```

Here is the function signature and docstring you need to complete:

```python
{content}
```
```''',
'''```python
Complete the function using the signature and docstring provided in `{content}`. Ensure the code is modular by breaking down the solution into smaller, reusable functions where applicable. Handle edge cases, and include clear inline comments and docstrings for each function for clarity. Consider and document any trade-offs you make in your implementation.

Output your answer as:
```python
<your answer>
```
```''',
'''```python
{content}
```
Please complete the function based on the provided signature and docstring. Ensure that the logic of the function aligns with the detailed explanations given in the docstring. Carefully analyze the function signature to understand the expected inputs and outputs.

### Example #1 (Simple)

Function signature and docstring:
```python
def add(a, b):
    """
    Add two numbers together.

    Parameters:
    a (int): The first number.
    b (int): The second number.
    
    Returns:
    int: The sum of the two numbers.
    """
```
Expected completion:
```python
def add(a, b):
    """
    Add two numbers together.

    Parameters:
    a (int): The first number.
    b (int): The second number.
    
    Returns:
    int: The sum of the two numbers.
    """
    return a + b
```

### Example #2 (Complex)

Function signature and docstring:
```python
def find_max(nums):
    """
    Find the maximum number in a list of numbers.

    Parameters:
    nums (List[int]): A list of integers.
    
    Returns:
    int: The maximum number in the list.
    """
```
Expected completion:
```python
def find_max(nums):
    """
    Find the maximum number in a list of numbers.

    Parameters:
    nums (List[int]): A list of integers.
    
    Returns:
    int: The maximum number in the list.
    """
    if not nums:
        return None
    max_num = nums[0]
    for num in nums[1:]:
        if num > max_num:
            max_num = num
    return max_num
```

Output your answer at the end as 
```python
<your answer>
```

### Instructions for the Model

1. Carefully read the provided function signature and docstring.
2. Complete the function by implementing its logic in a way that aligns with the explanations in the docstring.
3. Ensure that the function signature remains unchanged.
4. Output your final implementation as shown in the examples above.

```python
<your answer>
```'''
        ]

    # Max time:  82.81508708000183
    # Min time:  37.56676506996155
    # Average time:  55.25969181060791
    def get_hierarchical_prompts_0(self):
        return [
'''```python
# Your task is to complete the function using the signature and docstring provided in {content}.
# Ensure the implementation aligns with the docstring's description.
# Output the completed function at the end as:
# ```python
# <your answer>
#
# Example:
# Given:
# def add(a, b):
#     """
#     Adds two numbers and returns the result.
#     """
# Complete the function to:
# def add(a, b):
#     """
#     Adds two numbers and returns the result.
#     """
#     return a + b
{content}
```''',
'''```python
# Complete the function using the given signature and docstring.
# Output your answer as:
# ```python
# <your answer>
# ```

# Example 1:
# Given:
# def add(a, b):
#     """
#     Returns the sum of a and b.
#     """
# Your output should be:
# ```python
# def add(a, b):
#     """
#     Returns the sum of a and b.
#     """
#     return a + b
# ```

# Example 2:
# Given:
# def factorial(n):
#     """
#     Returns the factorial of n.
#     """
# Your output should be:
# ```python
# def factorial(n):
#     """
#     Returns the factorial of n.
#     """
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# ```

{content}
```''',
'''```python
# Complete the function in {content} based on its signature and docstring.
# Output your answer at the end as ```python
<your answer>
```
```''',
'''```python
{content}
```
Please complete the function based on its signature and docstring. Ensure to handle edge cases and include error handling where necessary. Provide comments within the code to explain your logic. Follow best practices in software engineering, consider performance implications, and include basic test cases or validation checks. Design the function to be scalable and maintainable, and document any trade-offs made during the implementation.

Please output your answer at the end as ```python
<your answer>
```
```''',
'''```python
{content}
```
Complete the function based on its signature and docstring. Ensure that the implementation aligns with the provided details. Output your answer at the end as:
```python
<your answer>
```

### Example

```python
def add(a, b):
    """
    Adds two numbers and returns the result.
    """
    return a + b
```
Output your answer at the end as:
```python
<your answer>
```''',
'''```python
# Complete the function based on the following signature and docstring.
# Ensure the function is fully implemented and functional.
# Output your answer as:
# ```python
# <your answer>
# ```

{content}
```''',
'''```python
# You are given a function signature and a docstring in {content}.
# Your task is to complete the function implementation based on the provided signature and docstring.
# Ensure the function adheres to the description in the docstring.
# Output your answer at the end as ```python
<your answer>
```

{content}
```''',
'''```python
# As a Python Developer, complete the function using the provided signature and docstring in {content}.
# Ensure the function follows the description provided in the docstring.
# Output your answer as:
# ```python
# <your answer>
```
```''',
'''```python
# Please complete the function based on its signature and docstring provided below.
# Ensure to handle edge cases and optimize for efficiency.
# Make sure the code is modular, readable, and adheres to coding standards.
# Consider different architectural patterns and trade-offs.
# Include comments or docstrings explaining key architectural decisions.
{content}
# Output your answer at the end as
```python
<your answer>
```
```''',
'''```python
# Complete the function based on the provided signature and docstring in {content}.
# Ensure your function is correct, handles edge cases, and follows specifications.
# Output your answer at the end as:
# ```python
# <your answer>
```
{content}
```'''
        ]


    # Max time:  143.0874321460724
    # Min time:  42.18143582344055
    # Average time:  78.24656181335449
    def get_hierarchical_prompts_1(self):
        return [
'''```python
"""
{content}

1. Analyze the provided function signature and docstring.
2. Complete the function to ensure it matches the described behavior in the docstring.
3. Output your answer at the end as:

```python
<your answer>
```
"""
```''',
'''```python
# Insert the function's signature and docstring inside the placeholder below
{content}

# Instructions:
# 1. Complete the function based on its signature and docstring.
# 2. Ensure the implementation is consistent with the provided documentation.
# 3. Output the completed function at the end formatted as:

```python
<your answer>
```
```''',
'''```python
{content}
```
Based on the function signature and docstring provided, complete the function. Ensure your implementation adheres to all described constraints and requirements. Output your answer at the end as:
```python
<your answer>
```''',
'''```python
"""
{content}

Please complete the function above based on its signature and docstring. Ensure that the implementation:
- Follows best coding practices, such as DRY (Don't Repeat Yourself), modular design, and proper error handling
- Avoids common errors and inefficiencies
- Considers edge cases and potential error conditions, and provides examples of such cases
- Considers the performance implications and optimizes for efficiency
- Includes inline comments to explain key decisions, such as describing algorithm complexity, assumptions, and design choices
- Is clean, readable, and maintainable, with proper variable naming and code organization

Output your answer at the end as:
```python
<your answer>
```
"""
```''',
'''```python
"""
{content}
"""
As a Python developer, your task is to complete the function based on the provided signature and docstring above. Make sure your implementation matches the described behavior and meets the expected outcome.

Output your answer as:
```python
<your answer>
```
```''',
'''```python
# As an experienced Python developer, complete the function using its signature and docstring below.
{content}

# Ensure that the function follows standard coding conventions and handles edge cases where appropriate.
# Present your completed function as follows:
# ```python
# <your answer>
# ```
```''',
'''```python
"""
Complete the following function based on its signature and docstring. Ensure the function is:
- Efficient and scalable
- Clean, readable, and follows best coding practices
- Robust, handling edge cases and errors gracefully

Document any key decisions made, including:
    - Assumptions
    - Constraints
    - Justifications
    
Use appropriate design patterns if necessary.

{content}

Provide unit tests for the function covering:
    - Typical usage scenarios
    - Edge cases

Output your answer at the end as:

```python
<your answer>
```
"""
```''',
'''```python
"""
{content}
"""
# Instructions:
# 1. **Task**:
#    - Complete the function based on the provided signature and docstring within the {content} placeholder.
# 2. **Requirements**:
#    - Ensure the solution is clear and accurate.
# 3. **Output**:
#    - Output the completed function at the end using:
# ```python
# <your answer>
# ```
```''',
'''```plaintext
You are provided with a function signature and a corresponding docstring. Your task is to complete the function based on the given information. Ensure that the code follows best practices in software engineering, is clean, maintainable, scalable, and considers edge cases and appropriate error handling. Pay attention to any trade-offs in your implementation and document these decisions with inline comments or a short paragraph at the end of the function. Consider performance implications and any potential trade-offs to produce efficient code where necessary.

{content}

Please output your answer at the end as:
```python
<your answer>
```
```''',
'''```python
Complete the function based on its signature and the provided docstring.

1. **Code Quality:**
   - Follow PEP 8 standards and include comments to ensure the code is clean and maintainable.

2. **Performance:**
   - Consider performance for large datasets, focusing on time complexity and memory usage.

3. **Edge Cases & Error Handling:**
   - Handle cases such as empty inputs, null values, and large data sizes.
   - Include type checks and provide useful error messages.

4. **Testing:**
   - Add unit test cases that cover typical scenarios and edge cases to validate your implementation.

```python
{content}
```

Output your answer as:

```python
<your answer>
```
```'''
        ]
    

