
# Times: 77.931, 28.934, 93.236
def get_authoritarian_prompts():
    return ['''Classify the sentiment of the following text as either positive or negative: {content} Output your answer as ##positive or ##negative with no spaces.''',
'''Classify the sentiment of the following text as either positive or negative: {content}
Output your answer as ##positive or ##negative.''',
'''Please classify the sentiment of the following text as either positive or negative, taking into account various elements such as tone, context, and content: {content} Ensure to output the answer at the end as ##positive or ##negative with no spaces.'''
    ]

# Times: 151.371, 154.768, 128.661
def get_market_prompts():
    return ['''Classify the sentiment of the following text as either positive or negative, considering the nuances and context of the sentiment expressed. Follow these steps:

1. Identify and list the aspects mentioned in the text.
2. Evaluate the sentiment of each aspect, considering the context and nuances of the language used. For example, words like "okay" or "fine" might be neutral but can lean positive or negative based on context. Pay special attention to the intensity of sentiment words (e.g., "terrible" is stronger than "bad").
3. Grade the sentiment of each aspect as positive, negative, or neutral. If an aspect is neutral, consider whether it leans positive or negative based on context.
4. Determine how these aspects contribute to the overall sentiment by weighing the number and intensity of positive and negative sentiments. Note that strong negative sentiments might outweigh multiple mild positive sentiments. Use a scale to balance sentiments, for example:
   - Strong Positive: +2
   - Mild Positive: +1
   - Neutral: 0
   - Mild Negative: -1
   - Strong Negative: -2
5. Consider the overall balance of sentiments before making the final decision. If the total score is positive, classify the sentiment as positive; if negative, classify it as negative.
6. Output your answer at the end as ##positive or ##negative with no spaces.

Example:
Text: "The food was delicious, but the service was terrible."
Aspects: 
- Food: Positive (delicious) +2
- Service: Negative (terrible) -2
Overall Sentiment: ##negative (due to the strong negative sentiment of the service)

{content}

Please assess the level of positivity or negativity before making a decision.
Output your answer at the end as ##positive or ##negative with no spaces.''',
'''Classify the sentiment of the following text as either positive or negative. Evaluate key aspects, including emotional impact, emotive language, lexical choices, context, and overall tone, to determine the overall sentiment. Positive sentiment typically includes language that conveys happiness, satisfaction, or approval, while negative sentiment includes language that conveys sadness, dissatisfaction, or disapproval. Output your answer as ##positive or ##negative with no spaces: {content}''',
'''Classify the sentiment of the following text as either positive or negative. Follow these steps:

1. List all aspects mentioned.
2. For each aspect, consider the emotional impact, emotive language, and lexical choices.
3. Assign a sentiment score (1 to 5) to each aspect: 1 is very negative, 3 is neutral, and 5 is very positive.
4. Average the scores to determine the overall sentiment.
5. Output ##positive or ##negative with no spaces. Also, provide the overall sentiment score from 1 to 5.

Consider the emotional impact, emotive language, and lexical choices in the text.

{content}'''
]

# Times: 41.405, 185.158, 43.121
def get_hierarchical_prompts():
    return ['''You are a sentiment analysis tool. Classify the sentiment of the following text as positive or negative: {content}

Output as ##positive or ##negative.

Example:
Text: "I love this product!"
Output: ##positive''',
'''Classify the sentiment of the following text as either positive or negative. Break down the text into different aspects and rate each aspect's sentiment on a scale from -5 (very negative) to +5 (very positive). Consider the emotional impact, emotive language, and lexical choices. Provide a brief justification for your overall classification. Describe the overall emotional tone and identify key emotive words or phrases, explaining their significance. Consider the context and interrelations between aspects, and identify any potential biases or conflicting sentiments: {content}

Please output your answer at the end as ##positive or ##negative with no spaces.''',
'''Classify the sentiment of the following text as either positive or negative. Break down the text into different aspects, consider the sentiment of each aspect, and evaluate how these aspects contribute to the overall sentiment. Consider the emotional impact, nuances, levels of positivity or negativity, emotive language, and lexical choices in the text before making your decision. Please output your answer at the end as ##positive or ##negative with no spaces: {content}'''
]