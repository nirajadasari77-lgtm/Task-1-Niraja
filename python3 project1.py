#Decode Lab Internship Project1
#Rule-Based AI Chatbot
print("WELCOME TO DECODE LABS RULE-BASED AI CHATBOT")
responses = {
    "hi": "Hello! Welcome to the Rule-Based AI Chatbot.",
    
    "hello": "Hi there! How can I assist you today?",
    
    "how are you": "I am functioning properly and ready to help.",
    
    "your name": "I am a Rule-Based AI Chatbot developed using Python.",
    
    "who created you": "I was created as part of an AI internship project.",
    
    "what is ai": "Artificial Intelligence is the simulation of human intelligence by machines.",
    
    "what is python": "Python is a powerful programming language widely used in AI, Machine Learning, and Data Science.",
    
    "what is machine learning": "Machine Learning enables computers to learn patterns from data and make predictions.",
    
    "what is data science": "Data Science involves collecting, analyzing, and interpreting data to gain insights.",
    
    "what courses do you recommend": "I recommend learning Python, Data Structures, DBMS, Machine Learning, and AI fundamentals.",
    
    "what is your purpose": "My purpose is to demonstrate rule-based conversation using predefined responses.",
    
    "help": "You can ask me about AI, Python, Machine Learning, Data Science, or my purpose.",
    
    "thank you": "You're welcome. Happy learning and best wishes for your internship!",
    
    "good morning": "Good morning! I hope you have a productive day ahead.",
    
    "good evening": "Good evening! How may I assist you today?"
}
while True:
    user=input("you entered:").lower().strip()

    #exit command
    if user == "bye":
        print("Bot: Goodbye!")
        break
    #default response
    reply = responses.get(
        user,
        "Bot: Sorry, I don't understand that."
    )

    print(reply)
    print("type 'bye' to exit")