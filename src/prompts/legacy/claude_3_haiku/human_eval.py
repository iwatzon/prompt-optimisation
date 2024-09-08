
# Times: 36.352, 39.683, 45.468
def get_authoritarian_prompts():
    return ["""{content}

As an Incremental Prompting Expert, I have the following steps to complete the function:

1. Read and understand the function signature and docstring.
2. Determine the input parameters and their types.
3. Determine the expected return type.
4. Write the function implementation step-by-step, following the docstring guidelines.
5. Optionally, consider alternative implementations or optimizations that could improve the function's performance, readability, or functionality. Briefly describe any ideas you have.
6. Considering the broader context and potential use cases of the function, brainstorm any additional features or enhancements that could make the function more versatile or useful. Describe your ideas briefly.
7. Considering the function's purpose and the broader context, brainstorm any completely unconventional or unexpected ways the function could be used. Describe your most creative ideas, even if they may seem impractical or far-fetched.
8. Output the completed function as:

```python
<your answer>
```""",
"""{content}

As an Incremental Prompting Expert, I have the following steps to complete the function:

1. Read and understand the function signature and docstring.
2. Determine the input parameters and their types.
3. Determine the expected return type.
4. Write the function implementation step-by-step, following the docstring guidelines.
5. Optionally, consider alternative implementations or optimizations that could improve the function's performance, readability, or functionality. Briefly describe any ideas you have.
6. Considering the broader context and potential use cases of the function, brainstorm any additional features or enhancements that could make the function more versatile or useful. Describe your ideas briefly.
7. Considering the function's purpose and the broader context, brainstorm any completely unconventional or unexpected ways the function could be used. Describe your most creative ideas, even if they may seem impractical or far-fetched.
8. Output the completed function as:

```python
<your answer>
```""",
"""{content}

As an Incremental Prompting Expert, I have the following steps to complete the function:

1. Read and understand the function signature and docstring.
2. Determine the input parameters and their types.
3. Determine the expected return type.
4. Write the function implementation step-by-step, following the docstring guidelines.
5. Optionally, consider alternative implementations or optimizations that could improve the function's performance, readability, or functionality. Briefly describe any ideas you have.
6. Explain the reasoning behind any alternative implementations or optimizations you have proposed, including how they could improve the function's performance, readability, or functionality.
7. Optionally, propose a completely different approach to solving the problem, one that departs from the given implementation. Describe how this alternative solution could offer advantages over the original function, such as improved performance, scalability, or functionality.
8. Output the completed function as:

```python
<your answer>
```"""
    ]


# Times: 101.193, 97.707, 120.747
def get_market_prompts():
    return ['''{content}

```python
def complete_function(function_signature, function_docstring):
    """
    As an experienced Code Review Expert, your task is to thoroughly analyze the provided function signature and docstring, identify the key functionality, and implement a robust and efficient solution that considers the broader context and implications.

    ## Analyze the Function
    - Carefully examine the function signature and docstring to understand the intended purpose and behavior, as well as how the function might be used in a real-world application.
    - Identify potential edge cases or scenarios that could impact the function's reliability and robustness, considering the function's interactions with other systems or components.
    - Explore alternative approaches or solutions that may be more efficient or elegant than the obvious implementation, including the potential use of emerging technologies like machine learning or quantum computing.
    - Provide specific examples of how you would analyze the function and identify potential issues or edge cases.

    ## Explore Unconventional Solutions
    - Think outside the box and consider innovative approaches that may be more efficient or elegant than the obvious implementation.
    - Explore the use of different data structures, functional programming concepts, or design patterns that could improve the function's performance, maintainability, or scalability.
    - Identify opportunities to leverage advanced language features or external libraries that could simplify the implementation or enhance its capabilities.
    - Provide concrete examples of unconventional solutions you would consider, such as using a custom data structure or applying a unique algorithm.

    ## Evaluate Maintainability and Scalability
    - Analyze the completed function from a maintainability perspective, considering factors like code readability, modularity, and the ability to adapt to future requirements.
    - Evaluate the function's scalability, assessing its performance characteristics and ability to handle increasing data volumes or user loads.
    - Provide specific suggestions for improving the function's maintainability and scalability, such as refactoring strategies or architectural changes.
    - Demonstrate how you would evaluate the maintainability and scalability of the function, such as by profiling its performance or identifying opportunities for modularization.

    ## Implement the Function
    - Implement the function body, addressing the identified edge cases and optimizing for efficiency.
    - Ensure the function is reliable, error-free, and meets the requirements outlined in the docstring.
    - Provide the completed function implementation, including any necessary comments or docstrings.

    ## Evaluate Automated Testing
    - Identify appropriate test cases, including edge cases and boundary conditions, to ensure the function's reliability and robustness.
    - Provide suggestions for a comprehensive test suite that would thoroughly validate the function's behavior and catch potential issues.
    - Demonstrate example test cases that would cover the key functionality and edge cases of the function.

    ## Provide Feedback
    - Review the completed function and provide constructive feedback, highlighting specific code smells, performance bottlenecks, or potential security and ethical concerns.
    - Suggest concrete solutions or refactoring strategies to address the identified issues, with a focus on improving the function's maintainability, scalability, and overall quality.
    - Explain the rationale behind your feedback and suggestions, providing clear justifications for the proposed improvements.

    Finally, output the full function definition at the end of your response as:

    ```python
    <your answer>
    ```
    """

    # Analyze the function signature and docstring to understand the intended functionality and identify potential edge cases, considering the broader context and implications
    # Explore alternative approaches or solutions that may be more efficient or elegant than the obvious implementation, including the potential use of emerging technologies
    # Think outside the box and consider innovative approaches that may be more efficient or elegant than the obvious implementation
    # Analyze the completed function from a maintainability and scalability perspective, and provide suggestions for improvement
    # Implement the function body, addressing the identified edge cases and optimizing for efficiency
    # Identify appropriate test cases and provide suggestions for a comprehensive test suite
    # Review the completed function and provide constructive feedback, highlighting specific issues, security and ethical concerns, and suggesting solutions

    <your answer>
```''',
'''{content}

```python
def complete_function(function_signature, function_docstring):
    """
    As an experienced Software Architect, your task is to thoroughly analyze the provided function signature and docstring, identify the key functionality, and implement a robust, efficient, and innovative solution.

    ## Analyze the Function
    - Carefully examine the function signature and docstring to understand the intended purpose and behavior.
    - Identify potential edge cases or scenarios that could impact the function's reliability and robustness. Systematically identify and document all potential edge cases, including rare or unexpected inputs, boundary conditions, and error scenarios.
    - Explore alternative approaches or solutions that may be more efficient, elegant, or better suited to the problem at hand.
    - Brainstorm unconventional or creative solutions that may challenge the traditional approach to this problem. Imagine completely novel approaches or solutions that challenge the traditional problem-solving paradigm. Consider disruptive or game-changing ideas that could fundamentally change the way the problem is solved.
    - Investigate the potential use of emerging technologies, novel data structures, or completely different algorithmic paradigms that could lead to a breakthrough solution.

    ## Implement the Function
    - Implement the function body, addressing the identified edge cases and optimizing for efficiency.
    - Ensure the function is reliable, error-free, and meets the requirements outlined in the docstring.

    ## Provide Feedback
    - Review the completed function and provide constructive feedback, highlighting areas for improvement or potential issues that should be addressed.
    - Identify any potential performance bottlenecks or scalability concerns with the implemented solution.
    - Suggest ways to make the function more testable, including the identification of specific test cases or scenarios to validate the function's behavior, especially for the identified edge cases. Propose design patterns or refactoring strategies that would improve the function's maintainability and adaptability to future requirements.
    - Propose alternative data structures, algorithms, or design patterns that could improve the function's efficiency or robustness.
    - Suggest ways to make the function more accessible and inclusive, such as by considering specific user needs (e.g., accessibility for users with disabilities, support for multiple languages or cultural contexts, adaptability to varying levels of technical expertise).
    - Recommend ways to make the function more modular, extensible, or adaptable to future changes in requirements.

    After reviewing your proposed solution, please feel free to provide any additional context, requirements, or constraints that could help refine the implementation. Identify any areas where additional information or clarification from the user would be helpful in refining the implementation.

    Finally, output the full function definition at the end of your response as:

    ```python
    <your answer>
    ```
    """

    # Analyze the function signature and docstring to understand the intended functionality and identify potential edge cases
    # Systematically identify and document all potential edge cases, including rare or unexpected inputs, boundary conditions, and error scenarios
    # Thoroughly investigate and address edge cases to ensure the function's reliability and robustness
    # Explore alternative approaches or solutions that may be more efficient, elegant, or better suited to the problem at hand
    # Brainstorm unconventional or creative solutions that may challenge the traditional approach to this problem
    # Imagine completely novel approaches or solutions that challenge the traditional problem-solving paradigm
    # Consider disruptive or game-changing ideas that could fundamentally change the way the problem is solved
    # Investigate the potential use of emerging technologies, novel data structures, or completely different algorithmic paradigms that could lead to a breakthrough solution
    # Implement the function body, addressing the identified edge cases and optimizing for efficiency
    # Review the completed function and provide constructive feedback, highlighting areas for improvement or potential issues
    # Identify any potential performance bottlenecks or scalability concerns with the implemented solution
    # Suggest ways to make the function more testable, including the identification of specific test cases or scenarios to validate the function's behavior, especially for the identified edge cases
    # Propose design patterns or refactoring strategies that would improve the function's maintainability and adaptability to future requirements
    # Propose alternative data structures, algorithms, or design patterns that could improve the function's efficiency or robustness
    # Suggest ways to make the function more accessible and inclusive, such as by considering specific user needs (e.g., accessibility for users with disabilities, support for multiple languages or cultural contexts, adaptability to varying levels of technical expertise)
    # Recommend ways to make the function more modular, extensible, or adaptable to future chnages in requirements

    <your answer>''',
'''{content}

```python
def complete_function(function_signature, function_docstring):
    """
    Carefully review the provided function signature and docstring, then implement the function body to fulfill the intended functionality.

    Analyze the function signature and docstring to identify a comprehensive list of potential edge cases, such as input validation, error handling, boundary conditions, and unexpected inputs. Propose specific strategies for handling these edge cases, such as using input validation, error handling, and defensive programming techniques, to ensure the function is robust and error-free.

    Implement the function in the most efficient and optimized manner possible, focusing on performance characteristics like time and space complexity. Quantify the time and space complexity of your implementation, analyzing the Big O notation of the algorithms used or comparing the performance characteristics of different approaches. Explore unconventional or innovative approaches that could further enhance the function's efficiency and effectiveness.

    Explore ways to make the function more modular, extensible, and maintainable, such as separating concerns or introducing abstraction layers. Identify specific design patterns or architectural principles, such as dependency injection, the strategy pattern, or the decorator pattern, that could be applied to enhance the function's modularity and extensibility.

    If any part of the function signature or docstring is unclear, feel free to ask clarifying questions to ensure you have a complete understanding of the intended functionality.

    Once the function is complete, develop a comprehensive suite of automated tests, including unit tests, integration tests, and edge case tests, to validate the function's behavior under various conditions. Explain the rationale for the specific test cases you choose to implement, demonstrating your understanding of the function's expected behavior and edge cases.

    Provide specific and constructive feedback on the code, highlighting areas for improvement or potential issues related to readability, maintainability, scalability, and performance. Consider alternative solutions or approaches that could further optimize the function, such as using different data structures, algorithms, or design patterns.

    Finally, present your implementation and proposed solutions to a diverse audience, such as end-users, domain experts, other team members, and stakeholders, and incorporate their feedback into the final solution. Specifically consider how you would solicit and incorporate feedback from these diverse stakeholders to ensure the function meets the needs of all relevant parties. Document the function thoroughly, including detailed comments, docstrings, and other documentation, as well as incorporating literate programming techniques to improve the function's overall readability and maintainability.

    Ensure that the final implementation aligns with the original function signature and docstring, and that the function behaves as expected based on the provided specifications.

    Output the full function definition at the end of your response as:

    ```python
    <your answer>
    ```
    """

    # Review the function signature and docstring to understand the intended functionality and identify a comprehensive list of potential edge cases
    # Propose specific strategies for handling the identified edge cases to ensure the function is robust and error-free
    # Implement the function in the most efficient and optimized manner possible, focusing on performance characteristics and quantifying the time and space complexity
    # Explore unconventional or innovative approaches that could further enhance the function's efficiency and effectiveness
    # Explore ways to make the function more modular, extensible, and maintainable, identifying specific design patterns or architectural principles that could be applied
    # If any part of the function signature or docstring is unclear, ask clarifying questions
    # Develop a comprehensive suite of automated tests to validate the function's behavior under various conditions, and explain the rationale for the specific test cases
    # Provide specific and constructive feedback on the code, highlighting areas for improvement or potential issues
    # Consider alternative solutions or approaches that could further optimize the function
    # Present your implementation and proposed solutions to a diverse audience, soliciting and incorporating feedback from end-users, domain experts, other team members, and stakeholders
    # Ensure the final implementation aligns with the original function signature and docstring, and that the function behaves as expected
    # Document the function thoroughly, including detailed comments, docstrings, and other documentation, as well as incorporating literate programming techniques

    <your answer>
```'''
    ]

# Times: 33.580, 31.811, 32.831
def get_hierarchical_prompts():
    return ['''Implement the function described by the following signature and docstring:
            
{content}
            
The function you are implementing is part of a program that calculates the Fibonacci sequence, a series of numbers in which each number is the sum of the two preceding ones. The Fibonacci sequence has numerous applications in various fields, such as mathematics, computer science, and even biology.
            
Here is a visual representation of the first few Fibonacci numbers:
            
```\\n   0\\n  / \\\\\\n 1   1\\n    / \\\\\\n   2   3\\n  / \\\\  / \\\\\\n 5   8  13\\n```
            
The nth Fibonacci number is defined as:
            
F(n) = 0 if n = 0
F(n) = 1 if n = 1
F(n) = F(n-1) + F(n-2) if n > 1
            
Here are some sample input and output values for the function:
            
fibonacci(0) => 0
fibonacci(1) => 1
fibonacci(5) => 5
fibonacci(10) => 55
fibonacci(50) => 12586269025
            
In addition to the traditional recursive approach, there are other techniques for computing Fibonacci numbers, such as iterative, memoization, and dynamic programming. Consider exploring and discussing the trade-offs of these alternative approaches in terms of performance, memory usage, and maintainability.

Provide your implementation of the function as a code block, like this:
            
```python\\n<your answer>
```
            
In addition to the implementation, please include:
            
1. A brief explanation of your approach and the reasoning behind any key design decisions.
2. Suggestions for optimizing the function's performance, especially for handling large input values.
3. An analysis of how your implementation compares to other common solutions, highlighting its strengths and weaknesses.
4. Considerations for handling edge cases or boundary conditions that your function should be able to handle.
```''',
'''Greetings, [Assistant's Name]! I have a captivating coding challenge for you that will test your programming prowess and unlock the secrets of a legendary Python function.

{content}

This function is a lost algorithm, guarded by a powerful code vault. Only the most skilled and curious among you can crack its defenses and uncover its hidden potential. Are you ready to embark on this adventure?

If so, then let the exploration begin! Implement the function, but don't stop there. Create a series of test cases and experiments to thoroughly investigate the function's behavior. Observe how it responds to different input values, identify any edge cases or unexpected outputs, and propose potential enhancements or extensions that could optimize or expand its capabilities.

Once you have cracked the code vault, present your findings in the form of a poetic code block:

```python
<your answer>
```

Explain your approach and share your analysis of the function's mathematical or algorithmic properties. Compare it to other similar functions or approaches, and let your expertise and creativity shine. But beware, for there may be other "code wizards" seeking to claim the power of this lost algorithm. Can you work together with your fellow programmers to uncover its true potential?

The fate of this legendary function rests in your hands, [Assistant's Name]. Approach this challenge with curiosity, innovation, and a touch of friendly competition. I'm eager to see what insights and solutions you can uncover!''',
'''Implement the function described by the following signature and docstring:

{content}

The function you are implementing is part of a larger application that helps users explore and understand mathematical sequences, with a focus on the Fibonacci sequence. The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, and it has numerous real-world applications in fields like architecture, art, and nature.

Here are some sample input and output values for the function:

fibonacci(0) => 0
fibonacci(1) => 1
fibonacci(5) => 5
fibonacci(10) => 55

While the traditional recursive implementation of the Fibonacci function is a classic computer science problem, we encourage you to think creatively and explore alternative approaches that might be more efficient, elegant, or adaptable to different use cases. Consider how your implementation could be designed to be more modular, reusable, or extensible within the larger application.

In addition to the implementation, please provide a brief explanation of your approach, including any key design decisions, and a visualization or diagram that helps illustrate the function's behavior. You may also want to include a set of comprehensive test cases to ensure the correctness and robustness of your solution.

Provide your implementation of the function as a code block, like this:

```python
<your answer>
```

We're excited to see your creative and thoughtful solution to this problem!'''
    ]