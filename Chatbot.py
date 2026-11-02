import re

def chatbot(user_input):
    user_input = user_input.lower()

    if re.search(r"\b(hi|hello|hey)\b", user_input):
        return "Hello! How can I help you?"

    elif "your name" in user_input:
        return "I am a simple chatbot."

    elif "how are you" in user_input:
        return "I am fine! Thank you."

    elif "bye" in user_input:
        return "Goodbye! Have a nice day!"

    else:
        return "Sorry, I don't understand."

print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user = input("You: ")
    response = chatbot(user)
    print("Chatbot:", response)

    if re.search(r"\bbye\b", user.lower()):
        break
