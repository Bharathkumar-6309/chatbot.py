# chatbot.py

print("Bot: Hello! I'm ChatBot. Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower().strip()

    if user_input in ["hi", "hello", "hai", "hey"]:
        print("Bot: Hello there! How can I help you today?")
    
    elif "how are you" in user_input:
        print("Bot: I'm just a program, but I'm doing great! Thanks for asking.")
    
    elif "your name" in user_input:
        print("Bot: I'm a rule-based chatbot created using Python.")
    
    elif "what can you do" in user_input:
        print("Bot: I can chat with you using simple logic! Try asking me something.")
    
    elif "help" in user_input:
        print("Bot: Sure! You can ask me about my name, what I do, or just say hi!")
    
    elif "bye" in user_input or "exit" in user_input:
        print("Bot: Goodbye! Have a nice day 😊")
        break
    
    elif "thank" in user_input:
        print("Bot: You're welcome!")

    elif "who" in user_input or "what" in user_input or "why" in user_input:
        print("Bot: Hmm, I'm not sure about that. I’m still learning.")

    else:
        print("Bot: I'm sorry, I didn't understand that. Can you try something else?")
