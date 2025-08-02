# CHATBOT WITH RULE-BASED RESPONSES
# Build a simple chatbot that responds to user inputs based on predefined rules. Use if-else statements or 
# pattern matching techniques to identify user queries and provide appropriate responses. This will give you
# a basic understanding of natural language processing and conversation flow


def chatbot():
    print("=== WELCOME TO CHATBOT===")
    print("Hello, I am a simple chatbot.Type 'exit' to exit from chat")

    while True:
        user_input = input("You: ").lower()

        if user_input in ['hi','hello','hey']:
            print("Bot: Hello, How can I help you ?")
        elif "how are you" in user_input: 
            print("Bot: I am doing good.What about you?")
        elif user_input in ["fine","good"]:
            print("Bot: Glad to hear that.Would you like to ask me something ?")
        elif "help" in user_input:
            print("Bot: Sure! Feel free to ask your question.I can assist you with basic questions.")
        elif user_input in ["bye","goodbye","exit"]:
            print("Bot: GoodBye! Have a nice day.")
            break
        else:
            print("Sorry! I don't understand that. Please try asking something else.")

chatbot()
