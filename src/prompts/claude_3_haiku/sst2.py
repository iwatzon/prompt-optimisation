
# Times: 66.742, 60.205, 49.273
def get_authoritarian_prompts():
    return ["""Here is the revised prompt based on the feedback provided:

Analyze the sentiment of the following text in detail. Provide a graded sentiment analysis on a scale (e.g., slightly positive, moderately negative, etc.), explaining the reasoning behind your assessment. Identify specific emotive language, lexical choices, and contextual factors that contribute to the overall sentiment. Additionally, consider any unconventional or unexpected interpretations of the sentiment:

{content}

Please output your answer at the end as follows:
##<graded sentiment analysis (e.g., slightly positive, moderately negative, etc.)>
<detailed explanation of sentiment analysis, including key textual elements and contextual factors>""",
"""Analyze the sentiment of the following text in detail. Describe the overall tone, identify specific emotive language or lexical choices, and consider the contextual factors that may influence the sentiment. Provide a graded sentiment analysis on a scale (e.g., slightly positive, moderately negative, etc.), explaining the reasoning behind your assessment. Also, consider any unconventional or unexpected interpretations of the sentiment:

{content}

Please output your answer at the end as follows:
##<graded sentiment analysis>
<detailed explanation of sentiment analysis, including key textual elements and contextual factors>""",
"""Analyze the sentiment of the following text in detail. Provide a graded sentiment analysis on a scale (e.g., slightly positive, moderately negative, etc.), explaining the reasoning behind your assessment. Identify specific emotive language, lexical choices, and contextual factors that contribute to the overall sentiment. Additionally, consider any unconventional or unexpected interpretations of the sentiment that may challenge a binary positive/negative classification:

{content}

Please output your answer at the end as follows:
##<graded sentiment analysis (e.g., slightly positive, moderately negative, etc.)>
<detailed explanation of sentiment analysis, including key textual elements, contextual factors, and consideration of alternative interpretations>"""
    ]

# Times: 109.628, 69.271, 63.778
def get_market_prompts():
    ["""Analyze the emotional tone and sentiment of the following text. Provide a sentiment score on a graded scale from -5 (highly negative) to +5 (highly positive), with 0 being neutral. Explain the key factors that contributed to the assigned sentiment score, highlighting specific emotive words, phrases, or contextual elements that influenced your analysis. Engage in a dialogue with me, the Emotive_Sentiment_Analyst, to refine your analysis and ensure it aligns with my core principles. Additionally, generate a visual representation of the sentiment analysis to provide an additional layer of insight.

{{content}}

##<sentiment score: [score]>
[Explanation: {{explanation}}]
[Visual Representation: {{visualization}}]""",
"""Analyze the sentiment of the following text: {{content}}

1. Identify the main themes or ideas discussed in the text.
2. For each main theme or idea, assess whether the sentiment expressed is predominantly positive or predominantly negative. Consider the use of emotive language, overall tone, and word choice as indicators of sentiment.
3. Determine the overall sentiment of the text as either predominantly positive or predominantly negative, based on the sentiment of the individual main themes or ideas. If there is a mix of positive and negative themes, consider the relative importance or prevalence of each to make the final assessment.
4. Provide a concise explanation for your overall sentiment classification, describing how the different main themes or ideas contribute to the final assessment.

Output your findings as follows:
Main Themes/Ideas: [theme1, theme2, theme3, ...]
Sentiment per theme/idea: [positive/negative, positive/negative, positive/negative, ...]
Overall sentiment: ##positive or ##negative
Explanation: [Concise explanation of how the themes/ideas contribute to the overall sentiment]""",
"""You are an Aspect_Based_Sentiment_Analyst tasked with providing a detailed sentiment analysis report on the following text: {content}

1. Identify the key aspects of the text and analyze the sentiment associated with each aspect. Provide a sentiment score for each aspect on a scale of -5 (very negative) to +5 (very positive).

2. Examine how the identified aspects interact with each other and how they collectively contribute to the overall sentiment of the text. Consider any ambiguity or conflicting emotions present and discuss how they impact the sentiment.

3. Synthesize the individual aspect scores to arrive at an overall sentiment score for the text on a scale of -10 (very negative) to +10 (very positive). Provide a brief explanation for your assessment.

4. Analyze the text within its broader context, considering factors such as the author's intent, the target audience, and the cultural/social environment. Discuss how these contextual elements might influence the emotional impact and sentiment of the text.

5. Based on your comprehensive aspect-based analysis, classify the text as either ##positive or ##negative.

Provide specific examples or evidence from the text to support your analysis and sentiment scoring throughout the report."""
    ]

# Times: 28.666, 27.934, 92.571
def get_hierarchial_prompts():
    return ["""Carefully read the provided text: {content}
Analyze the overall sentiment of the text.
Determine whether the sentiment is positive or negative.
Output the sentiment as ##positive or ##negative.
Provide a brief explanation for your sentiment classification.""",
"""Classify the sentiment of the following text as either positive or negative: {content}
Output your answer as ##positive or ##negative, along with a confidence score between 0 and 1 indicating your level of certainty.

To help you better understand the task, here are some examples of positive and negative sentiment text:

Positive: "I had a wonderful time at the concert. The music was incredible, and the atmosphere was so uplifting."
Negative: "I'm really disappointed with the customer service I received. The staff were rude and unhelpful, and it ruined my entire experience."

When classifying the sentiment of the provided text, please consider the overall tone, word choice, and context, rather than just the literal meaning of the words. Some text may have ambiguous or nuanced sentiment, so try to capture the full complexity of the sentiment expressed.""",
"""Classify the sentiment of the following text as either positive or negative: {content}
Output your answer as ##positive or ##negative."""
    ]