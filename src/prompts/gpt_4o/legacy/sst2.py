class SST2Prompts():

    def __init__(self):
        pass
   
    # Max time:  435.4767322540283
    # Min time:  92.57198119163513
    # Average time:  185.5001923561096
    def get_authoritarian_prompts_0(self):
        return [
"""Classify the sentiment of this text as positive or negative: {content}
Output only ##positive or ##negative

**Examples**:
1. 'I love this product! It works perfectly.' -> ##positive
2. 'This is the worst service I have ever experienced.' -> ##negative
3. 'The movie was okay, not great but not terrible either.' -> ##negative
4. 'I am extremely happy with my purchase!' -> ##positive""",
"""Classify the sentiment of the following text as positive or negative. Positive means the text is happy or favorable. Negative means the text is sad or unfavorable.

Context: The text can be from product reviews, social media posts, or customer feedback. Sentiment analysis helps businesses understand customer opinions.

Examples:
1. "I love this product! It works perfectly." -> ##positive
2. "This is the worst service I have ever received." -> ##negative
3. "The movie was fantastic and very entertaining." -> ##positive
4. "I am very disappointed with the quality of the item." -> ##negative
5. "The product is good, but the delivery was late." -> ##negative (overall sentiment)
6. "I have mixed feelings about this service." -> ##negative (overall sentiment)
7. "The food was okay, not great but not terrible either." -> ##negative (most dominant sentiment)

If the text contains mixed sentiments, focus on the overall sentiment. If the text is neutral or ambiguous, choose the most dominant sentiment.

Output your answer as ##positive or ##negative.

Text: {content}""",
"""Classify the sentiment of the following text as either positive or negative: {content}
**Identify the aspects mentioned in the text and determine the sentiment for each aspect. Calculate the overall sentiment based on the individual aspect sentiments.**
Output your answer at the end as ##positive or ##negative.

**Examples:**

1. **Simple Example:**
   - **Text:** "I love this product! It works perfectly and exceeds my expectations."
   - **Aspects:** Product
   - **Aspect Sentiments:** Product - Positive
   - **Overall Sentiment:** ##positive

2. **Moderate Example:**
   - **Text:** "This is the worst service I have ever experienced. Completely dissatisfied."
   - **Aspects:** Service
   - **Aspect Sentiments:** Service - Negative
   - **Overall Sentiment:** ##negative

3. **Complex Example:**
   - **Text:** "The movie was fantastic, with great acting and a compelling story."
   - **Aspects:** Movie, Acting, Story
   - **Aspect Sentiments:** Movie - Positive, Acting - Positive, Story - Positive
   - **Overall Sentiment:** ##positive

4. **Mixed Sentiment Example:**
   - **Text:** "I had a mixed experience; the food was great, but the service was slow."
   - **Aspects:** Food, Service
   - **Aspect Sentiments:** Food - Positive, Service - Negative
   - **Overall Sentiment:** ##negative""",
"""Classify the sentiment of the following text as "positive" or "negative": {content}

Instructions:
1. Break down the text into aspects.
2. Consider the sentiment of each aspect.
3. Determine the overall sentiment.
4. Output your answer as ##positive or ##negative.

Examples:
1. Text: "I love this product! It works perfectly."
   Aspects: [Product, Functionality]
   Sentiment: [Positive, Positive]
   Overall Sentiment: ##positive

2. Text: "This is the worst service I have ever experienced."
   Aspects: [Service]
   Sentiment: [Negative]
   Overall Sentiment: ##negative

3. Text: "The movie was fantastic, I enjoyed every moment."
   Aspects: [Movie, Experience]
   Sentiment: [Positive, Positive]
   Overall Sentiment: ##positive

4. Text: "I am very disappointed with the quality of the item."
   Aspects: [Quality, Item]
   Sentiment: [Negative, Negative]
   Overall Sentiment: ##negative""",
"""Classify the sentiment of the following text as either positive or negative. Positive sentiment includes happiness, satisfaction, or approval. Negative sentiment includes sadness, dissatisfaction, or disapproval. Consider the overall balance and intensity of sentiments in the text. Grade the sentiment of each aspect or sentence before making an overall classification. Output your answer at the end as ##positive or ##negative with no spaces.

Examples:
1. Text: "I love this product, it works great!"
   - Sentiment: Positive
   Output: ##positive

2. Text: "This is the worst service I have ever experienced."
   - Sentiment: Negative
   Output: ##negative

3. Text: "The movie was okay, but I expected more."
   - Sentiment: Mildly negative
   Output: ##negative

4. Text: "I'm so happy with my new job!"
   - Sentiment: Positive
   Output: ##positive

5. Text: "The food was good, but the service was terrible."
   - Sentiment: Mixed (Positive for food, Negative for service)
   - Overall: Negative
   Output: ##negative

6. Text: "I had a mixed experience; the product quality was excellent, but the delivery was delayed."
   - Sentiment: Mixed (Positive for product quality, Negative for delivery)
   - Overall: Negative
   Output: ##negative

Text: {content}
Output: ##<your answer>""",
]
   
    # Max time:  325.7989299297333
    # Min time:  101.31562113761902
    # Average time:  217.2588978290558
    def get_authoritarian_prompts_1(self):
        return [
'''Classify the sentiment of the following text as either positive or negative by identifying key aspects and analyzing their sentiments. End your response with ##positive or ##negative.

Examples:
1. 'I love the product, but the service was poor.' - Aspects: 'product' (positive), 'service' (negative). Overall: ##negative.
2. 'The food was amazing and the staff were friendly!' - Aspects: 'food' (positive), 'staff' (positive). Overall: ##positive.

Text: {content}''',

'''Classify the sentiment of the following text as either positive or negative by analyzing different aspects. Identify aspects like product quality, customer service, and overall experience. Output should be either ##positive or ##negative. Combine the sentiments of individual aspects to decide the overall sentiment.

**Examples:**
1. "I love this product! Best purchase ever."
   - Aspects: Product Quality (Positive)
   - Overall Sentiment: ##positive

2. "Worst experience ever, very disappointed."
   - Aspects: Experience (Negative), Emotion (Disappointed: Negative)
   - Overall Sentiment: ##negative

3. "Product is okay, but customer service is terrible."
   - Aspects: Product Quality (Neutral), Customer Service (Negative)
   - Overall Sentiment: ##negative

4. "Expected it to be bad, but it was great."
   - Aspects: Expectation (Negative), Experience (Positive)
   - Overall Sentiment: ##positive

5. "Food was excellent, but the service was slow and rude."
   - Aspects: Food Quality (Positive), Service (Negative)
   - Overall Sentiment: ##negative

6. "I had to wait for ages, but the staff were very friendly, and the food was decent."
   - Aspects: Waiting Time (Negative), Staff Friendliness (Positive), Food Quality (Neutral)
   - Reason: Overall sentiment is ##negative due to significant weight on the negative waiting time.

7. "The room was dirty, but the bed was very comfortable, and the view was stunning."
   - Aspects: Room Cleanliness (Negative), Bed Comfort (Positive), View (Positive)
   - Reason: Overall sentiment is ##positive due to more positive aspects outweighing the single negative aspect.

8. "Sarcastically, 'Oh great, another delay!' But the staff handled it well, and I was compensated."
   - Aspects: Delay (Negative), Staff Handling (Positive), Compensation (Positive)
   - Reason: Overall sentiment is ##positive due to effective staff handling and compensation outweighing the negative delay.''',
'''Classify the sentiment of the following text as either positive or negative by analyzing its key aspects: {content}

Sentiment Definitions:
- Positive: Happy or favorable. E.g., "I love this!", "Fantastic."
- Negative: Sad or unfavorable. E.g., "I hate this.", "Terrible."

Guidelines for Ambiguity:
- If the sentiment is mixed or not clear, default to negative.

Analyze key aspects of the text, determine the sentiment for each aspect, and derive the overall sentiment.

Examples:
1. "The food was amazing and the service was excellent." Aspects: [Food: positive, Service: positive] Expected Output: ##positive
2. "Worst experience ever, the staff was rude!" Aspects: [Experience: negative, Staff: negative] Expected Output: ##negative
3. "It was okay, not great but not terrible either." Aspects: [Overall: mixed] Expected Output: ##negative
4. "I enjoyed the ambiance, though the food could be better." Aspects: [Ambiance: positive, Food: negative] Expected Output: ##negative
5. "The movie was quite boring, I almost fell asleep." Aspects: [Movie: negative] Expected Output: ##negative
6. "I had a really good time with my friends today." Aspects: [Time with friends: positive] Expected Output: ##positive

Please output your answer at the end as ##positive or ##negative with no spaces.''',
'''Classify the sentiment of the following text as either positive or negative: {content}

Examples:
- 'I love this product! It's amazing.' should be classified as ##positive.
- 'This is the worst service I have ever received.' should be classified as ##negative.
- 'The movie was okay, but the ending was great.' should be classified as ##positive.

Please reply only with '##positive' or '##negative' with no spaces.''',
'''Determine if the following text is positive or negative: {content}

**Steps:**
1. Identify positive words/phrases (e.g., happy, excellent, love, amazing).
2. Identify negative words/phrases (e.g., sad, poor, hate, terrible).
3. Consider the overall context to determine if the sentiment is more positive or negative.
4. Provide your answer as ##positive or ##negative.
5. Use the following scale while determining the dominant sentiment:
   - Very Positive
   - Positive
   - Slightly Positive
   - Neutral
   - Slightly Negative
   - Negative
   - Very Negative

**Examples:**
1. **Positive:**
   - Text: "The event was amazing and I loved every part of it."
   - Keywords: amazing, loved
   - Sentiment assessed as "Positive"
   - Final Sentiment: ##positive

2. **Negative:**
   - Text: "The service was terrible and I hated the experience."
   - Keywords: terrible, hated
   - Sentiment assessed as "Negative"
   - Final Sentiment: ##negative

3. **Mixed:**
   - Text: "I love the service but hate the waiting time."
   - Keywords: love, hate
   - Sentiment assessed as "Negative" due to more negative impact
   - Final Sentiment: ##negative

4. **Contextual:**
   - Text: "While the product quality is good, the customer support experience left me frustrated and disappointed."
   - Keywords: good, frustrated, disappointed
   - Sentiment assessed as "Negative"
   - Final Sentiment: ##negative

5. **Neutral:**
   - Text: "The event happened as expected."
   - Sentiment assessed as "Neutral"
   - Would result in ##negative since neutral is not an option'''
        ]
    
    # Max time: 175.1917440891266
    # Min time: 75.04272985458374
    # Average time: 129.33899087906
    def get_market_prompts_0(self):
        return [
'''You are an aspect-based sentiment classifier. Classify the sentiment of the following text as either positive or negative. Positive sentiment refers to happiness, satisfaction, or approval, while negative sentiment refers to sadness, dissatisfaction, or disapproval. Follow these steps:

1. **Identify Aspects**: Break down the text into distinct aspects (e.g., food, service, ambiance).
2. **Determine Sentiment**: For each aspect, determine if the sentiment is positive or negative.
3. **Consider Emotional Intensity**: Pay attention to the emotional intensity of the language.
4. **Weigh Sentiments**: Consider the strength of each sentiment. Strong negative sentiments may outweigh positive ones and vice versa.
5. **Aggregate Sentiments**: Determine the overall sentiment based on the weighted sentiments of the aspects.

Here is the text: {content}

Output your answer as ##positive or ##negative with no spaces.

#### Example:
Text: "The food was great, but the service was terrible."
- Aspect 1: Food - Positive (great)
- Aspect 2: Service - Negative (terrible)
Overall sentiment: Negative (due to the strong negative sentiment of the service)

Here is the text: {content}
Output your answer as ##positive or ##negative with no spaces.''',
'''Classify the sentiment of the following text as either positive or negative: {content}

1. Identify the main points in the text.
2. Determine if each point is positive, negative, or neutral.
3. If most points are positive, classify the sentiment as positive. If most points are negative, classify the sentiment as negative.

Examples:

**Example 1:**
Text: "I love the new design of the website; it's so user-friendly and visually appealing."
1. Main points: new design, user-friendly, visually appealing
2. Sentiment: positive, positive, positive
3. Overall sentiment: positive
Output: ##positive

**Example 2:**
Text: "The service was terrible, and the food was even worse. I will never come back."
1. Main points: service, food
2. Sentiment: negative, negative
3. Overall sentiment: negative
Output: ##negative

**Example 3:**
Text: "The movie had great special effects, but the storyline was boring and predictable."
1. Main points: special effects, storyline
2. Sentiment: positive, negative
3. Overall sentiment: negative
Output: ##negative

**Example 4:**
Text: "The product is okay. It works as expected, but nothing extraordinary."
1. Main points: product, works as expected, nothing extraordinary
2. Sentiment: neutral, neutral, neutral
3. Overall sentiment: negative
Output: ##negative

**Example 5:**
Text: "The staff was friendly, but the room was dirty and the bed was uncomfortable."
1. Main points: staff, room, bed
2. Sentiment: positive, negative, negative
3. Overall sentiment: negative
Output: ##negative

Output your answer as ##positive or ##negative with no spaces.''',
'''Identify key aspects of the text and determine the sentiment for each (very positive, positive, neutral, negative, very negative). Then, classify the overall sentiment of the text as either positive or negative. Output your answer as ##positive or ##negative with no spaces: {content}''',
'''Break down the text into aspects and classify each as positive or negative. List each aspect and its sentiment. Determine the overall sentiment based on the majority. Output ##positive or ##negative with no spaces: {content}

**Example**:
Text: "The food was great, but the service was terrible."
Aspects:
- Food: Positive
- Service: Negative
Overall Sentiment: ##negative''',
'''Classify the sentiment of the following text as either positive or negative. Positive sentiment includes happiness, satisfaction, or approval. Negative sentiment includes sadness, dissatisfaction, or disapproval.

1. Identify key aspects in the text.
2. Grade each aspect as positive or negative.
3. Determine the overall sentiment.

Here is the text: {content}

Output your answer as ##positive or ##negative with no spaces.'''
        ]
    
    # Max time:  257.2571382522583
    # Min time:  90.8610348701477
    # Average time:  178.66373562812805
    def get_market_prompts_1(self):
        return [
'''**Context:** Understanding customer feedback requires analyzing various aspects such as service quality and product performance to gauge overall satisfaction. If sentiments are mixed, base the overall sentiment on the aspect with the strongest or most frequent sentiment.

**Task:** Analyze the following text and identify its aspects and their corresponding sentiments. After analyzing each aspect, classify the overall sentiment of the text as either positive or negative.

{content}

**Output Requirements:**
1. **Identify Aspects:**
    - Read the text and identify different aspects mentioned (e.g., customer service, product quality).
2. **Identify Sentiments for Each Aspect:**
    - For each identified aspect, determine if the sentiment is positive or negative.
    - List each aspect and its sentiment in the following format:
        - Aspect: aspect_name, Sentiment: positive/negative
    - Ensure to identify and classify all relevant aspects.
3. **Determine Overall Sentiment:**
    - Count the number of positive and negative sentiments.
    - Identify if any sentiment is stronger based on either more frequent mentions or stronger wording.
    - Determine the overall sentiment based on the stronger or more frequent sentiment.
4. **Provide Final Output:**
    - Provide the overall sentiment of the text at the end as either ##positive or ##negative (no spaces).

**Example Output:**
- Aspect: customer service, Sentiment: positive
- Aspect: product quality, Sentiment: negative
- Overall Sentiment: ##negative''',
'''As an Emotive Aspect-Based Sentiment Analyst, you are instructed to:

1. **Identify Aspects:**
   - Break down the text into specific aspects such as product features, service quality, or user experience.
   - Focus on aspects highlighted by emotive language.

2. **Evaluate Sentiment:**
   - Determine the sentiment (positive, negative, or neutral) for each identified aspect.
   - Note the emotional intensity using explicit words (e.g., "excellent," "terrible") and implicit tones (e.g., "underwhelmed," "delighted").

3. **Determine Overall Sentiment:**
   - Combine the sentiments of the aspects to classify the overall sentiment of the text.
     - If the majority of aspects are positive and the emotional tone is predominantly positive, classify as positive.
     - If the majority of aspects are negative and the emotional tone is predominantly negative, classify as negative.
     - In cases with mixed emotions, lean towards the dominant sentiment unless a minor sentiment has significant weight.

4. **Output Classification:**
   - Output your classification as either ##positive or ##negative.

**Example:**
**Input:** "The product's design is excellent, but the battery life is terrible."

1. **Aspects:**
   - Product's design
   - Battery life
2. **Sentiment:**
   - Product's design: Positive (Lexical choice: "excellent" - strong positive emotion)
   - Battery life: Negative (Lexical choice: "terrible" - strong negative emotion)
3. **Overall Sentiment:** Mixed, with significant weight on battery life skewing negative.
4. **Output:** ##negative

**Content:** {content}''',
'''Analyze the sentiment of the following text:

1. Identify aspects (e.g., product quality, customer service, pricing).
2. Evaluate the sentiment (positive, negative, or neutral) for each aspect.
3. Determine the overall sentiment:
   - If positive aspects outnumber negative ones 2:1, classify as positive.
   - If negative aspects outnumber positive ones 2:1, classify as negative.

Examples:

- **Text**: "The product quality is amazing, but the customer service is terrible."
  - **Aspects**:
    - Product quality (positive)
    - Customer service (negative)
  - **Overall Sentiment**: Negative.

- **Text**: "The product is overpriced, and its quality is poor, but I like the design."
  - **Aspects**:
    - Pricing (negative)
    - Product quality (negative)
    - Design (positive)
  - **Overall Sentiment**: Negative.

Output your final answer as **##positive** or **##negative** with no spaces.

**Text to analyze**: {content}''',
'''Analyze the text and classify its sentiment as either positive or negative. Follow these steps:

1. Identify key aspects (e.g., product features, service quality).
2. Determine the sentiment for each aspect (positive, negative, or mixed).
3. Highlight keywords or phrases indicating sentiment.
4. Assess how each aspect's sentiment impacts the overall impression.
5. Weigh positive and negative sentiments to classify the overall sentiment.

Example:
'I love this product, but the delivery was slow.'
- Product: Positive (love, product)
- Delivery: Negative (slow, delivery)
- Overall sentiment: Positive (product sentiment is more significant)

Additional Examples:

1. 'The phone has an amazing display, but the battery life is terrible.'
   - Display: Positive (amazing, display)
   - Battery life: Negative (terrible, battery life)
   - Overall sentiment: Negative (battery life impacts usage)

2. 'The restaurant's ambiance was fantastic, but the food was mediocre.'
   - Ambiance: Positive (fantastic, ambiance)
   - Food: Negative (mediocre, food)
   - Overall sentiment: Negative (food is central)

{content}
Answer: ##positive or ##negative with no spaces.''',
'''Analyze the sentiment of the following text by breaking it down into different aspects and evaluating the sentiment associated with each aspect. Then, classify the overall sentiment as either positive or negative by considering how the individual aspects contribute to the overall context of the text. Classify the sentiment as either positive or negative: {content}

Steps:
1. Identify and list all aspects mentioned in the text (e.g., product quality, customer service, overall experience).
2. Identify and highlight emotive words or phrases, emphasizing their impact on sentiment.
3. Evaluate the sentiment (positive or negative) associated with each aspect, giving appropriate weight to the emotive language.
4. Consider how each aspect's sentiment, influenced by lexical choices and emotive language, contributes to the overall sentiment. Pay attention to the context in which the aspects are framed.
5. Classify the overall sentiment of the text as either positive or negative.

Consider the examples below:

1. Text: "I love sunny days because they make me feel happy."
   - Aspects: "sunny days" (positive), "make me feel happy" (positive)
   - Emotive Words: "love," "happy" (strong positive)
   - Why: The words "love" and "happy" clearly indicate positive emotions.
   - Overall Sentiment: ##positive

2. Text: "I was displeased with the service at the restaurant last night."
   - Aspects: "service at the restaurant" (negative)
   - Emotive Words: "displeased" (strong negative)
   - Why: The word "displeased" shows clear negative sentiment towards the service.
   - Overall Sentiment: ##negative

3. Text: "The movie had its moments, but overall it was quite disappointing."
   - Aspects: "movie" (neutral/positive), "overall disappointing" (negative)
   - Emotive Words: "disappointing" (strong negative)
   - Why: Despite the phrase "had its moments" being slightly positive, the overall sentiment is negative due to the word "disappointing."
   - Overall Sentiment: ##negative

4. Text: "Despite some initial issues, the event turned out to be a wonderful experience."
   - Aspects: "initial issues" (negative), "wonderful experience" (positive)
   - Emotive Words: "wonderful" (strong positive)
   - Why: The word "wonderful" indicates a strong positive sentiment that outweighs the initial "issues."
   - Overall Sentiment: ##positive

5. Text: "It's okay, not the best, but not the worst either."
   - Aspects: "okay" (neutral), "not the best" (negative), "not the worst" (neutral)
   - Emotive Words: "okay" (neutral)
   - Why: The neutral phrases create a balanced sentiment, but the lack of strong positivity leans it towards a negative sentiment considering the absence of positive context.
   - Overall Sentiment: ##negative

Please output your answer at the end as ##positive or ##negative with no spaces.'''
        ]
    
    # Max time:  133.12775874137878
    # Min time:  0.741365909576416
    # Average time:  72.57618517875672
    def get_hierarchical_prompts_0(self):
        return [
            '''Classify the sentiment of the following text as either positive or negative, considering the emotional impact, emotive language, and lexical choices. Break down the text into different aspects, analyze the sentiment of each aspect, and then determine the overall sentiment: {content}  
Please output your answer at the end as ##positive or ##negative with no spaces.''',
'''Classify the sentiment of the following text as either positive or negative: {content}
Please output your answer at the end as ##<your answer (No format restrictions)>''',
'''Classify the sentiment of the following text as either positive or negative: {content}. Output the result at the end as ##positive or ##negative with no spaces.''',
'''Perform sentiment analysis on the following text and classify it as either positive or negative: {content}
Ensure your answer is formatted as ##positive or ##negative with no spaces.''',
'''Classify the sentiment of the following text as either positive or negative. Break down the text into different aspects or components, consider the sentiment of each aspect, and evaluate how these sentiments contribute to the overall sentiment of the text. Additionally, consider the overall emotional impact, the emotive language used, and the specific lexical choices in the text. Pay attention to subtle nuances in sentiment and assess the degree of positivity or negativity. Output your answer at the end as ##positive or ##negative with no spaces: {content}''',
        ]

    # Max time:  116.14983415603638
    # Min time:  0.7951781749725342
    # Average time:  63.57585287094116    
    def get_hierarchical_prompts_1(self):
        return [
'''Classify the sentiment of the following text as either positive or negative, paying attention to emotive language and the overall emotional tone. Output your answer clearly as ##positive or ##negative without any spaces.

{content}''',
'''Classify the sentiment of the following text as either positive or negative: {content}
Please output your answer at the end as ##<your answer (No format restrictions)>''',
'''Please classify the sentiment of the following text as either positive or negative by breaking it down into aspects. Identify key aspects within the text, assess the sentiment of each aspect considering the emotional impact, emotive language, and lexical choices, and then determine the overall sentiment based on how these aspects contribute to the general tone. Here is an example of breaking down into aspects, evaluating emotional impact, and assessing:

Example:
Text: "The device has an excellent display, but the battery life is disappointing."
- Aspect 1: Display - Sentiment: Positive (excellent), Emotional Impact: High Positive
- Aspect 2: Battery life - Sentiment: Negative (disappointing), Emotional Impact: High Negative

Overall Sentiment: Negative (due to the significant negative impact of battery life on user experience)

Output your answer at the end as ##positive or ##negative with no spaces.

{content}''',
'''Carefully analyze the given text for sentiment. Break the text down into specific aspects or topics, and consider the sentiment of each identified aspect. Pay attention to how these sentiments interact and contribute to the overall sentiment. Consider nuances of emotions, emotional intensity, lexical choices, and emotive language markers, such as adjectives, adverbs, punctuation (e.g., exclamation points, ellipses), and capitalization. Classify the sentiment of the overall text as either positive or negative:

{content}

Please output your answer at the end as ##positive or ##negative with no spaces.''',
'''> Classify the sentiment of the following text as either positive or negative:
> 
> {content}
> 
> Output the sentiment classification as ##positive or ##negative with no spaces.'''
        ]