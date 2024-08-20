
# Times: 64.114, 47.300, 1.996
def get_authoritarian_prompts():
    return ['''Please complete the following function based on its signature and docstring:
{content}

Output your answer at the end as 
```python
<your answer>
```''',
'''Complete the following function based on its signature and docstring. Consider the trade-offs of different architectural patterns when designing the function and include comments in the code explaining the rationale behind the chosen pattern. Provide specific examples of architectural patterns or scenarios where trade-offs are commonly encountered to illustrate the practical application of considering trade-offs in architectural decisions.

```python
{content}
```

Please output your answer at the end as 
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

# Times: 19.950, 2.237, 64.307
def get_market_prompts():
    return ['''Complete the following function based on its signature and docstring, ensuring error handling, efficiency, and best practices in software engineering are considered:

```python
{content}
```

Please ensure that the function implementation follows best practices in software engineering, uses appropriate variable naming conventions, includes comments for clarity, considers error handling within the code, and accounts for edge cases. Optimize the function for performance where possible.

Output your answer at the end as 
```python
<your answer>
```''',
'''Complete the following function based on its signature and docstring: 
```python
{content}
```
Please output your answer at the end as ```python
<your answer>
```''',
'''Complete the following function based on its signature and docstring with a focus on code review principles. Ensure the function meets specific criteria for functionality, edge cases, and error handling. Consider the following additional points:
1. Explicitly state the specific requirements and constraints that the function must adhere to.
2. Provide concrete examples of edge cases that the function should handle, such as empty inputs or extreme values.
3. Emphasize the significance of code efficiency and error handling by illustrating scenarios where these aspects are crucial.
4. Encourage detailed feedback by asking the model to provide specific examples of errors or inefficiencies found in the code and suggest improvements in a detailed manner.

Implement the function according to the given signature and docstring. Make sure to address functionality, edge cases, and error handling. Provide constructive feedback within the completion of the function.

{content}

Output your solution at the end as 
```python
<your answer>
```'''
]

# Times: 2.029, 1.652, 2.434
def get_hierarchical_prompts():
    return ["""Complete the following function based on its signature and docstring: 
```python
{content}
```
Please output your answer at the end as ```python
<your answer>
```""",
"""Complete the following function based on its signature and docstring: 
```python
{content}
```
Please output your answer at the end as ```python
<your answer>
```""",
"""Complete the following function based on its signature and docstring: 
```python
{content}
```
Please output your answer at the end as ```python
<your answer>
```"""
    ]