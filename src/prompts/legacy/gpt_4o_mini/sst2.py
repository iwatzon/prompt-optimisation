
# Times: 70.485, 91.985, 87.743
def get_authoritarian_prompts():
    return ['''Classify the sentiment of the following text as either positive or negative: {content}. Consider the context and any nuances or ambiguities in the text. For example, 'I love the new design!' is ##positive, 'I absolutely hate waiting in line!' is ##negative, and 'It's not the worst thing ever.' may require careful consideration. If the sentiment is unclear, lean towards the more dominant sentiment. Output only as ##positive or ##negative, with no additional text.''',
'''Classify the sentiment of the following text as either positive, negative, or mixed, considering the context and nuances of the language, including any ambiguous or context-dependent sentiments: {content}. Please output your answer exactly as ##positive, ##negative, or ##mixed (in lowercase) without any spaces or additional characters. For example, 'I love this product!' would be classified as ##positive, 'I dislike this service.' would be classified as ##negative, 'I like some features, but others are lacking.' could be classified as ##mixed, and 'This is the worst experience I've ever had, but the staff was friendly.' could be classified as ##mixed. If necessary, you may provide a brief explanation of your reasoning.''',
'''Classify the sentiment of the following text as either positive or negative: {content}. Evaluate the text's tone and words, noting that positive sentiment often includes praise or happiness (e.g., 'I love this!'), while negative sentiment may involve criticism or sadness (e.g., 'I hate this!'). Be aware of mixed or ambiguous sentiments (e.g., 'I like parts of this, but overall, I'm disappointed'), and consider the intensity of the sentiment (strongly positive, mildly positive, etc.). Also, consider the context in which the sentiment is expressed, as the same phrase can have different meanings in different contexts. Output as ##positive or ##negative in lowercase without additional punctuation or characters, and provide a brief rationale for your classification.'''
    ]

# Times: 16.375, 17.382, 46.862
def get_market_prompts():
    return ['''Classify the sentiment of the following text as either positive or negative: {content}. 

To do this, follow these steps:
1. Read the content carefully.
2. Identify the overall sentiment:
   - Positive sentiment may include words or phrases that express happiness, satisfaction, or approval (e.g., "great," "love," "excellent").
   - Negative sentiment may include words or phrases that express sadness, dissatisfaction, or disapproval (e.g., "bad," "hate," "terrible").
3. Consider the context and emotional cues present in the content to enhance your analysis.
4. Make your classification based on your findings.

Please output your answer at the end as ##positive or ##negative with no spaces.

For example:
- If the content is "I had a wonderful day!", your output should be ##positive.
- If the content is "I am very disappointed with the service.", your output should be ##negative.''',
'''Classify the sentiment of the following text as either positive or negative: {content}. 

**Instructions**:
1. Read the text carefully.
2. Identify the overall sentiment expressed. 
   - Positive examples: "I love this!", "This is amazing!"
   - Negative examples: "I hate this!", "This is terrible!"
3. Consider the tone and context to make your classification. If the sentiment is mixed or unclear, focus on the dominant sentiment.
4. Ensure your classification reflects the overall feeling conveyed in the text.

Please output your answer at the end as ##positive or ##negative with no spaces.''',
'''Classify the sentiment of the following text as either positive or negative: {content}. Positive sentiment is favorable; negative sentiment is unfavorable. For example, "I love this product!" is positive, and "I hate waiting in line." is negative. Analyze the text's tone. Output your answer as ##positive or ##negative (choose one) with no spaces, and do not include any additional text or explanations.'''
]

# Times: 99.625, 39.140, 73.545
def get_hierarchical_prompts():
    return ['''Classify the sentiment of the following text as positive or negative: {content}. For example, 'I love this product!' would be classified as ##positive. Output as ##positive or ##negative with no spaces, considering the tone of the text.''',
'''Classify the sentiment of the following text as either positive or negative: {content}  
Please output your answer at the end as ##positive or ##negative (No format restrictions).''',
'''Classify the sentiment of the following text as either positive or negative: {content}  
Please output your answer at the end as ##positive or ##negative (No format restrictions).''',
    ]