import random

greetings = ["Hello!", "Hi there!", "Greetings!", "How can I help you today?"]
questions = [
    "How's your day going?",
    "What are you up to?",
    "Anything interesting happening?",
    "What's on your mind?",
    "How can I assist you today?",
    "What's new with you?",
    "How are you doing today?",
    "What's going on?",
    "How's everything?",
    "What's up?",
    "How's life?",
    "How's everything going?",
    "What's happening?",
    "How's your day?",
    "What's new?",
    "How are you?",
    "How's it going?",
    "What's going on with you?",
    "How are things?",

]
follow_ups = {
    "good": ["That's awesome!", "Glad to hear it!", "Tell me more about it!"],
    "bad": ["Oh no, I'm sorry to hear that.", "Is there anything I can do to help?", "Maybe a joke will cheer you up?"],
    "ok": ["Just okay? Maybe we can find something to make it better.", "Want to talk about it?"],
    "nothing": ["Nothing? That's okay too. Sometimes it's nice to just relax.", "If you ever feel like talking, I'm here."],
}
topics = {
    "general": {
        "tell me a joke": ["Why did the scarecrow win an award? Because he was outstanding in his field!", "What do you call a fish with no eyes? Fsh!"],  # Add more jokes here
        "how are you": "I'm an AI, so I don't have feelings, but I'm functioning well. How about you?",
        "what's your name": "I'm a chatbot. You can call me ChatBot.",
    },
    "weather": {
        "default": "I'm not able to check the weather right now, but you can always step outside or look online.",
        "rain": "I love the rain! It's so calming.",
        "sun": "The sun is shining bright today! Perfect weather for a picnic.",
        "snow": "Do you want to build a snowman? ⛄",

    },
    "news": {
        "default": "For the latest news, I recommend checking reputable news websites or apps.",
        "covid": "The COVID-19 situation is constantly evolving. Stay updated by checking the CDC website.",
        "technology": "Technology is advancing rapidly. Check out tech news websites for the latest updates.",
        "politics": "Politics can be complex. Make sure to get information from multiple sources to stay informed.",

    },
    "coding": {
        "default": "Coding is a valuable skill to learn. There are many online resources available to help you get started.",
        "python": "Python is a versatile programming language used for web development, data analysis, artificial intelligence, and more.",
        "java": "Java is a popular programming language known for its portability and versatility.",
        "javascript": "JavaScript is commonly used for web development and adding interactivity to websites.",
        "html": "HTML is the standard markup language used to create and design web pages.",
        "css": "CSS is used to style the HTML elements and make web pages visually appealing.",
    },
}

def learn(topic, question, answer):
    """Associates keywords from the question to the provided answer within a specific topic."""
    if topic not in topics:
        topics[topic] = {}
    for word in question.split():
        if word.lower() not in topics[topic]:
            topics[topic][word.lower()] = answer

def get_response(question):
    question = question.lower()

    # Prioritize specific topics if mentioned
    for topic, responses in topics.items():
        if topic in question:
            for keyword, response in responses.items():
                if keyword in question:
                    if isinstance(response, list):
                        return random.choice(response)
                    return response
            return responses.get("default", "I'm still learning about that topic.")

    # Check for follow-up keywords
    for keyword, responses in follow_ups.items():
        if keyword in question:
            return random.choice(responses)

    # Check for greetings
    for greeting in greetings:
        if question in greeting.lower():
            return random.choice(questions)

    # If no match, indicate learning and provide a generic response
    learn("general", question, "I'm still learning about that.")
    return "That's an interesting question. I'll try to learn more about it!"

# Main conversation loop
print("Chatbot: " + random.choice(greetings))
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye! Have a great day!")
        break
    response = get_response(user_input)
    print("Chatbot: " + response)
