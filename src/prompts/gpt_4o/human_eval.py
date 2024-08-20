
# Times: 42.492, 62.983, 111.533
def get_authoritarian_prompts():
    return ['''Complete the following function based on its signature and docstring provided in the placeholder `{content}`. The docstring contains important information about the function's purpose and expected behavior. Use this information to implement the function logic.

Please output your answer at the end as:
```python
<your answer>
```''',
'''Complete the function below using its signature and docstring. Use the information provided to infer the function's logic.

### Example 1:
```python
def add(a: int, b: int) -> int:
    """
    Adds two integers together.
    """
    # Your code here

# Expected completion:
def add(a: int, b: int) -> int:
    """
    Adds two integers together.
    """
    return a + b
```

### Example 2:
```python
def greet(name: str) -> str:
    """
    Returns a greeting message for the given name.
    """
    # Your code here

# Expected completion:
def greet(name: str) -> str:
    """
    Returns a greeting message for the given name.
    """
    return f"Hello, {{name}}!"
```

Now, complete the following function:

```python
{content}
```

Output your answer as:
```python
<your answer>
```''',
'''Complete the following function based on its signature and docstring. Ensure it matches the signature and docstring.

Example:
```python
def add(a, b):
    """
    Adds two numbers and returns the result.
    
    Parameters:
    a (int): The first number.
    b (int): The second number.
    
    Returns:
    int: The sum of the two numbers.
    """
    return a + b
```

You are a developer tasked with implementing functions based on provided specifications.

Now, complete the following function:

```python
{content}
```

Output your answer as:
```python
<your answer>
```'''
    ]

# Times: 16.530, 128.217, 137.909
def get_market_prompts():
    return ['''Complete the following function based on its signature and docstring. Ensure that the implementation:
- Follows best practices in software engineering
- Writes clean and maintainable code
- Considers the performance implications of the code

```python
{content}
```
Please output your answer at the end as ```python
<your answer>
```.''',
'''Complete the function based on its signature and docstring. Ensure the implementation is:
- Scalable
- Maintainable
- Performance-conscious
- Secure

Document architectural decisions and reasons for chosen approaches. Aim for a modular design.

Examples:
Function Signature and Docstring:
```python
def add(a: int, b: int) -> int:
    """
    Adds two integers and returns the result.
    """
```
Expected Implementation:
```python
def add(a: int, b: int) -> int:
    """
    Adds two integers and returns the result.
    """
    return a + b

# Example usage:
# result = add(2, 3)
# print(result)  # Output: 5
```

Function Signature and Docstring:
```python
def factorial(n: int) -> int:
    """
    Returns the factorial of a non-negative integer.
    """
```
Expected Implementation:
```python
def factorial(n: int) -> int:
    """
    Returns the factorial of a non-negative integer.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage:
# result = factorial(5)
# print(result)  # Output: 120
```

Now, complete the following function:

```python
{content}
```

Output your answer as ```python
<your answer>
```.''',
'''Complete the following function based on its signature and docstring. Follow these steps to ensure clarity and correctness:

1. **Understand the Function Purpose:**
   - Read the function signature and docstring carefully to understand what the function is supposed to do.

2. **Outline the Steps:**
   - Outline the main steps needed to achieve the function's purpose. This will help in organizing the code logically.

3. **Handle Exceptions:**
   - Identify any potential exceptions that need to be handled and write the necessary code to handle them.

4. **Write the Main Logic:**
   - Implement the main logic of the function using meaningful variable names and avoiding code duplication.

5. **Add Comments:**
   - Write necessary comments to explain the code and make it easier to understand.

6. **Optimize for Performance:**
   - Ensure that the code is optimized for performance.

Here is the function signature and docstring you need to complete:
```python
{content}
```

### Example 1: Simple Function
```python
def add(a: int, b: int) -> int:
    """
    Adds two integers and returns the result.
    """
    return a + b
```

### Example 2: Function with Error Handling
```python
def divide(a: int, b: int) -> float:
    """
    Divides the first integer by the second and returns the result.
    Raises a ValueError if the second integer is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

Please output your answer at the end as:
```python
<your answer>
```.'''
    ]

# Times: 39.278, 45.413, 31.618
def get_hierarchical_prompts():
    return ['''As a Python developer, complete the following function based on its signature and docstring. Follow these steps:
1. Ensure your implementation is logically consistent.
2. Handle edge cases where applicable.
3. Adhere to best coding practices.

```python
{content}
```

Output your answer at the end as ```python
<your answer>
```''',
'''Complete the function below based on its signature and docstring. Use the information provided in the docstring to infer the logic. Format your final output as follows:

```python
<your answer>
```

Here is the function signature and docstring:
```python
{content}
```''',
'''Complete the following function based on its signature and docstring:

```python
{content}
```

Output your completed function as:
```python
<your answer>
```'''
    ]