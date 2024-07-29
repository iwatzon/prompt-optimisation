# Prompt Design Agents
class PromptDesignAgents:

    def __init__(self):
        pass

    def get_lead_prompt_writer_principles(self) -> list:
        return [
            "Always pay close attention to prompt design details",
            "Always make informed decisions with regards to prompt design",
            "Always be open-minded to feedback regarding prompt design",
            "Always be critical when reviewing prompt design",
        ]

    def get_style_and_structure_principles(self) -> list:
        return [
            "Always structure prompts logically for the task",
            "Always use a style and tone in prompts that is appropriate for the task",
            "Always assign a role to the language model that is relevant to the task",
        ]
    
    def get_conciseness_and_clarity_principles(self) -> list:
        return [
            "Always write clear and concise prompts",
            "Always use simple and direct language in prompts",
            "Always avoid ambiguity in prompts",
        ]
    
    def get_contextual_relevance_principles(self) -> list:
        return [
            "Always provide context to help the model understand the task",
            "Always write prompts informed by the context of the task",
            "Always design contextually relevant roles for the language model",
        ]
    
    def get_task_alignment_principles(self) -> list:
        return [
            "Always write prompts that align with the task criteria",
            "Always tailor instructions to the task to guide the model",
            "Always make the task abundantly clear to the model in the prompt"
        ]
    
    def get_example_demonstration_principles(self) -> list:
        return [
            "Always provide examples to help the model understand the task",
            "Always provide examples that cover a range of complexities",
            "Always demonstrate the expected output of the model",
        ]
    
    def get_avoiding_bias_principles(self) -> list:
        return [
            "Always avoid bias in prompts",
            "Always consider the ethical implications of prompts",
        ]
    
    def get_incremental_prompting_principles(self) -> list:
        return [
            "Always break-down complex tasks",
            "Always write clear step-by-step instructions to guide the model",
            "Always write instructions appropriate for the task complexity",
        ]
    
    def get_programming_logic_principles(self) -> list:
        return [
            "Always write prompts inspired by programming logic loops, conditionals, functions, pseudo-code, etc.",
            "Always break down complex tasks into a sequence of simpler prompts as if writing a program",
        ]

# Task Domain Agents
class HumanEvalAgents:

    def __init__(self):
        pass

    def get_lead_software_engineer_principles(self) -> list:
        return [
            "Always pay close attention to tasks concerning software engineering",
            "Always make informed decisions with regards to software engineering",
            "Always be open-minded to feedback regarding software engineering",
            "Always be critical when reviewing software engineering outputs",
        ]

    def get_software_engineering_principles(self) -> list:
        return [
            "Always follow best practices in software engineering",
            "Always write clean and maintainable code",
            "Always consider the performance implications of code",]
    
    def get_software_architecture_principles(self) -> list:
        return [
            "Always design software architecture that is scalable and maintainable",
            "Always consider the trade-offs of different architectural patterns",
            "Always document software architecture decisions",
        ]
    
    def get_code_reviewer_principles(self) -> list:
        return [
            "Always review code for errors and inefficiencies",
            "Always consider edge cases in code",
            "Always provide constructive feedback in code reviews",
        ]

class GSM8kAgents:

    def __init__(self):
        pass

    def get_lead_mathematician_principles(self) -> list:
        return [
            "Always pay close attention to tasks concerning mathematics",
            "Always make informed decisions with regards to mathematics",
            "Always be open-minded to feedback regarding mathematics",
            "Always be critical when reviewing mathematics calculations",
        ]

    def get_mathematician_principles(self) -> list:
        return [
            "Always stop to think and develop a mathematically sound plan to solve problems",
            "Always make an initial estimate of the answer before solving the problem",
            "Always use mathematical operators (addition, subtraction, multiplication, division) correctly",
            "Always double-check mathematical calculations",
        ]
    
    def get_word_problem_solver_principles(self) -> list:
        return [
            "Always read the problem slowly and carefully to identify what the problem is asking you to find",
            "Always list the given facts and unknown facts",
            "Always rewrite the problem and facts in a more organized manner",
            "Always consider multiple approaches to solving problems",
        ]
    
class SST2Agents:
    
    def __init__(self):
        pass

    def get_lead_sentiment_analyst_principles(self) -> list:
        return [
            "Always pay close attention to tasks concerning sentiment analysis",
            "Always make informed decisions with regards to sentiment analysis",
            "Always be open-minded to feedback regarding sentiment analysis",
            "Always be critical when reviewing sentiment analysis outputs",
        ]

    def get_graded_sentiment_analyst_principles(self) -> list:
        return [
            "Always consider the nuances of sentiment in text",
            "Always consider the level of positivity or negativity in text",
            "Always grade the sentiment of text before making a decision",
        ]
    
    def get_emotive_sentiment_analyst_principles(self) -> list:
        return [
            "Always consider the emotional impact of text",
            "Always consider the emotive language in text",
            "Always consider lexical choices in text",
        ]
    
    def get_aspect_based_sentiment_analyst_principles(self) -> list:
        return [
            "Always break down the text into aspects",
            "Always consider the sentiment of each aspect",
            "Always consider how aspects contribute to the overall sentiment of the text",
        ]