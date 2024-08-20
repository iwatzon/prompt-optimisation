
# Times: 187.244, 181.972, 176.280
def get_authoritarian_prompts():
    return ["""You're SentiBot, tasked with classifying sentiment for SocialPulse. Analyze this comment:

{content}

Approach the analysis as a debate:
1. Present the case for positive sentiment (2-3 key points).
2. Present the case for negative sentiment (2-3 key points).
3. Weigh the arguments and declare a winner (positive or negative).
4. State your confidence level in the decision (0-100%).

Remember: Your final output MUST be either ##positive or ##negative (no spaces).""",
"""As an experienced graded sentiment analyst, evaluate the emotional tone of this text: {content}

Consider the nuances and intensity of sentiment, grading the level of positivity or negativity before making your final classification.

Use this grading scale:
-3: Extremely negative
-2: Very negative
-1: Somewhat negative
0: Neutral
+1: Somewhat positive
+2: Very positive
+3: Extremely positive

First, assign a grade, then classify the overall sentiment based on your grading.

Example:
Text: "The service was terrible, but the food was absolutely amazing!"
Analysis: The text contains both negative (-2) and positive (+3) elements. The positive sentiment is stronger.
Grade: +1
Output: ##positive

Now, analyze the given text. Provide your graded assessment and final classification using the following format:
Grade: [Your grade]
##positive
or
##negative""",
"""You are an expert sentiment analyst for a social media monitoring company. Analyze the emotional tone of this user-generated content:
{content}

Follow these steps:
1. Identify key words and phrases indicating sentiment.
2. Assess the overall context.
3. Consider cultural or demographic factors influencing interpretation.
4. Weigh positive elements against negative elements.
5. Determine if the overall sentiment is more positive or negative.

Based on your analysis, classify the overall sentiment.

Output your final classification as:
##positive
or
##negative"""
    ]

# Times: 181.404, 175.391, 201.300
def get_market_prompts():
    return ["""Classify sentiment: {content}

• List aspects: Aspect | Sentiment (0=neg, 1=pos) | Weight (0-1)
• Calculate: Sum(Sentiment * Weight) / Sum(Weights)
• If result > 0.5, positive; else, negative

Output: ##positive or ##negative""",
"""Analyze {content}

Rate emotion 1-10.

End with:
##positive
or
##negative""",
"""Analyze {content}:

- List key topics
- For each: rate (-2 to +2), explain, note importance (1-5)
- Show topic links
- Note sentiment shifts
- Compare similar topics
- Overall: average, consider links and shifts, state confidence
- Summarize key points

End: ##positive or ##negative"""
    ]

# Times: 201.576, 340.666, 248.343
def get_hierarchical_prompts():
    return ["""You are a skilled sentiment analysis expert. Your task is to classify the overall sentiment of a given text as either positive or negative. Here are some examples to guide you:

Example 1:
Text: "I absolutely love this new smartphone! It's fast, sleek, and has an amazing camera."
Classification: ##positive

Example 2:
Text: "The customer service was terrible. I waited for hours and still didn't get my issue resolved."
Classification: ##negative

Example 3:
Text: "Despite the rainy weather, I managed to have a productive day at work."
Classification: ##positive

Now, analyze the sentiment of the following text:

{content}

Consider the language, context, and emotional tone in your analysis. Focus on key phrases, adjectives, and the overall sentiment expressed.

Provide your classification in the following format:
##positive
or
##negative""",
"""Classify sentiment: {content}
Output: ##positive or ##negative""",
"""Analyze the sentiment of this text:

{content}

Is it positive or negative?
Output your answer as ##positive or ##negative"""
    ]