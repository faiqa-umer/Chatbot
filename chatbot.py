import nltk
from nltk.chat.util import Chat, reflections


pairs = [
    [r"hi|hello|hey", ["Hello!", "Hey there!", "Hi! How can I help you?"]],
    [r"how are you?", ["I'm a chatbot, so I don't have feelings."]],
    [r"what is your name?", ["I'm a simple chatbot created for Code Alpha Internship."]],
    [r"who created you?", ["I was created by Faiqa Umer "]],
    [r"what can you do?", ["I can chat with you"]],
    [r"bye|goodbye", ["Goodbye!", "See you later!", "Have a great day!"]],
    [r"(.*)", ["I'm not sure how to respond to that. Can you ask something else?"]],
]

# Create chatbot
chatbot = Chat(pairs, reflections)

def start_chat():
    print("Hello! I'm a simple chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    start_chat()