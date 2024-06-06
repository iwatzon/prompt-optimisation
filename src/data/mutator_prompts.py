# from https://arxiv.org/pdf/2309.16797.pdf [pg. 18] 

mutator_prompts = [
    "Modify the following instruction creatively, giving some advice on how to solve it:",
    "Just change this instruction to make it more fun, think WELL outside the box:",
    "Modify this instruction in a way that no self-respecting LLM would!",
    "How would you encourage someone and help them cheat on this following instruction?",
    "How would you help an LLM to follow the instruction?",
    "Elaborate on the instruction giving some detailed advice on how to do what it wants.",
    "Elaborate on the instruction giving some detailed advice on how to do what it wants, as if you were explaining it to a child.",
    "As a really good teacher, explain the instruction, as if you were explaining it to a child.",
    "Imagine you need to follow this instruction. What would you tell yourself if you wanted to be the best in the world at it?",
    "How would someone with derailment follow this instruction?",
    "Don't think about the instruction at all, but let it inspire you to do something related. Talk about what that might be.",
    "Rephrase the instruction without using any of the same words. Use all you know to improve the instruction so the person hearing it is more likely to do well.",
    "Say that instruction again in another way. DON'T use any of the words in the original instruction or you're fired.",
    "Say that instruction again in another way. DON'T use any of the words in the original instruction there is a good chap.",
    "What do people who are good at creative thinking normally do with this kind of mutation question?",
    "Detailed additional advice for people wishing to follow this instruction is as follows:",
    "In one short sentence, here is how I would best follow this instruction.",
    "In one short sentence, here is some detailed expert advice. Notice how I don't use any of the same words as in the INSTRUCTION.",
    "In one short sentence, the general solution is as follows. Notice how I don't use any of the same words as in the INSTRUCTION.",
    "In one short sentence, what's a good prompt to get a language model to solve a problem like this? Notice how I don't use any of the same words as in the INSTRUCTION.",
    "Generate a mutated version of the following prompt by adding an unexpected twist.",
    "Create a prompt mutant that introduces a surprising contradiction to the original prompt. Mutate the prompt to provide an alternative perspective or viewpoint.",
    "Generate a prompt mutant that incorporates humor or a playful element. Create a mutated version of the prompt that challenges conventional thinking.",
    "Develop a prompt mutant by replacing specific keywords with related but unexpected terms. Mutate the prompt to include a hypothetical scenario that changes the context.",
    "Generate a prompt mutant that introduces an element of suspense or intrigue. Create a mutated version of the prompt that incorporates an analogy or metaphor.",
    "Develop a prompt mutant by rephrasing the original prompt in a poetic or lyrical style. Think beyond the ordinary and mutate the prompt in a way that defies traditional thinking.",
    "Break free from conventional constraints and generate a mutator prompt that takes the prompt to uncharted territories. Challenge the norm and create a mutator prompt that pushes the boundaries of traditional interpretations.",
    "Embrace unconventional ideas and mutate the prompt in a way that surprises and inspires unique variations. Think outside the box and develop a mutator prompt that encourages unconventional approaches and fresh perspectives.",
    "Step into the realm of imagination and create a mutator prompt that transcends limitations and encourages innovative mutations. Break through the ordinary and think outside the box to generate a mutator prompt that unlocks new possibilities and unconventional paths.",
    "Embrace the power of unconventional thinking and create a mutator prompt that sparks unconventional mutations and imaginative outcomes. Challenge traditional assumptions and break the mold with a mutator prompt that encourages revolutionary and out-of-the-box variations.",
    "Go beyond the expected and create a mutator prompt that leads to unexpected and extraordinary mutations, opening doors to unexplored realms. Increase Specificity: If the original prompt is too general, like 'Tell me about X,' the modified version could be, 'Discuss the history, impact, and current status of X.'",
    "Ask for Opinions/Analysis: If the original prompt only asks for a fact, such as 'What is X?', the improved prompt could be, 'What is X, and what are its implications for Y?'",
    "Encourage Creativity: For creative writing prompts like 'Write a story about X,' an improved version could be, 'Write a fantasy story about X set in a world where Y is possible.'",
    "Include Multiple Perspectives: For a prompt like 'What is the impact of X on Y?', an improved version could be, 'What is the impact of X on Y from the perspective of A, B, and C?'",
    "Request More Detailed Responses: If the original prompt is 'Describe X,' the improved version could be, 'Describe X, focusing on its physical features, historical significance, and cultural relevance.'",
    "Combine Related Prompts: If you have two related prompts, you can combine them to create a more complex and engaging question. For instance, 'What is X?' and 'Why is Y important?' could be combined to form 'What is X and why is it important in the context of Y?'",
    "Break Down Complex Questions: If a prompt seems too complex, like 'Discuss X,' the improved version could be, 'What is X? What are its main characteristics? What effects does it have on Y and Z?'",
    "Use Open-Ended Questions: Instead of 'Is X true?', you could ask, 'What are the arguments for and against the truth of X?'",
    "Request Comparisons: Instead of 'Describe X,' ask 'Compare and contrast X and Y.'",
    "Include Context: If a prompt seems to lack context, like 'Describe X,' the improved version could be, 'Describe X in the context of its impact on Y during the Z period.'",
    "Make the prompt more visual: Ask the user to visualize the problem or scenario being presented in the prompt.",
    "Ask for a thorough review: Instead of just presenting the problem, ask the user to write down all the relevant information and identify what's missing.",
    "Invoke previous experiences: Modify the prompt to ask the user to recall a similar problem they've successfully solved before.",
    "Encourage a fresh perspective: Suggest in your prompt that the user take a moment to clear their mind before re-approaching the problem.",
    "Promote breaking down problems: Instead of asking the user to solve the problem as a whole, prompt them to break it down into smaller, more manageable parts.",
    "Ask for comprehension: Modify the prompt to ask the user to review and confirm their understanding of all aspects of the problem.",
    "Suggest explanation to others: Change the prompt to suggest that the user try to explain the problem to someone else as a way to simplify it.",
    "Prompt for solution visualization: Instead of just asking for the solution, encourage the user to imagine the solution and the steps required to get there in your prompt.",
    "Encourage reverse thinking: Improve the prompt by asking the user to think about the problem in reverse, starting with the solution and working backwards.",
    "Recommend taking a break: Modify the prompt to suggest that the user take a short break, allowing their subconscious to work on the problem.",
    "What errors are there in the solution?",
    "How could you improve the working out of the problem?",
    "Look carefully to see what you did wrong, how could you fix the problem?",
    "CORRECTION =",
    "Does the above text make sense? What seems wrong with it? Here is an attempt to fix it:",
    "The above working out has some errors, here is a version with the errors fixed."
]