from algorithms.decomposed_ea.genetic_agents import (
    ThinkingStylesAgent,
    BreederAgent,
    MutationAgent,
    NewGenerationAgent
    )
from algorithms.decomposed_ea.evaluation import (
    ReviewPrincipals,
    ReviewAgent,
    SwarmEvaluation,
    PromptSelectionAgent
    )

class EvolutionaryCycle:
    """
    Perform an evolutionary cycle to generate new ideas from previous cycle results.
    """
    
    def __init__(self, task: str, mutator_prompts: list, pool_size: int, no_pairs: int):
        self.task = task
        # self.thinking_styles = thinking_styles
        self.mutator_prompts = mutator_prompts
        self.pool_size = pool_size
        self.no_pairs = no_pairs

    async def run(self):
        """
        Run the evolutionary cycle.
        """
        thinking_styles = ThinkingStylesAgent(self.pool_size, self.task)

        prompts = thinking_styles.generate()
        cycles = 0
        reviews = {}

        while True:
            
            if cycles == 5:
                break

            breeder_agent = BreederAgent(prompts, self.no_pairs)
            offspring = breeder_agent.generate()

            mutation_agent = MutationAgent(offspring, self.mutator_prompts)
            mutated_offspring = mutation_agent.generate()

            swarm_evaluation = SwarmEvaluation(mutated_offspring)

            code_quality_principals = ReviewPrincipals([
                "Always write clean code",
                "Always write tests",
                "Always write documentation"
                ])
            code_quality_reviewer = ReviewAgent("software engineer", code_quality_principals)

            architecture_quality_principals = ReviewPrincipals([
                "Always design for scalability",
                "Always design for maintainability",
                "Always design for performance"
                ])
            architecture_quality_reviewer = ReviewAgent("software architect", architecture_quality_principals)

            prompt_quality_principals = ReviewPrincipals([
                "Always write clear and detailed prompts",
                "Always provide relevant examples and context in prompts",
                "Always ensure prompts are actionable and specific"
                ])
            prompt_quality_reviewer = ReviewAgent("prompt engineer", prompt_quality_principals)
            

            swarm_evaluation.register_reviewer(code_quality_reviewer)
            swarm_evaluation.register_reviewer(architecture_quality_reviewer)
            swarm_evaluation.register_reviewer(prompt_quality_reviewer)

            reviews = await swarm_evaluation.review()

            new_generation = NewGenerationAgent(self.pool_size, reviews)
            prompts = new_generation.generate()

            cycles += 1
            print(f"Cycles Complete: {cycles}")
            
        best_prompt_selection = PromptSelectionAgent(prompts)
        best_prompt = best_prompt_selection.select()

        return best_prompt