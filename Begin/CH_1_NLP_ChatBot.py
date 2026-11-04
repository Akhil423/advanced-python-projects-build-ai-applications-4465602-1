from textblob import TextBlob
# Define intents and their corresponding responses based on keywords
intents ={
    "hours":{
        "keywords":["hours","open","close"],
        "response":"we are open from 10am to 8PM, Monday to Saturday"
    },
    "return":{
        "keywords":["refund","money back", "return"],
        "response":"i would be happy to help you with the return process, let me transfer to a live agent"
    }
}
def get_response(message):
    # Convert the message to lowercase for consistent keyword matching
    message = message.lower()
    # Check if the message contains any keywords associated with defined intents
   # int details =
    for intent, intent_data in intents.items():
        if any(word in message for word in intent_data["keywords"]):
         return intent_data["response"]
    # Analyze the sentiment of the message using TextBlob

        sentimentscore = TextBlob(message).sentiment.polarity
    # Return a response based on the sentiment score
    return ("That's great to hear!" if sentimentscore>0 else
               "So sorry to hear that, how can i help you?" if sentimentscore<0 else
               "I see, can you tell me more about that?")
    # Greet the user and prompt for input
def chat():
    print("Akki: Hi, How can i help you today?")   
    # Continuously prompt the user for input until they choose to exit
    while(user_message := input("You: ").strip().lower()) not in ["exit","quit","bye"]:
         print(f"\nChatBot: {get_response(user_message)}")
    # Thank the user for chatting when they exit
    print("ChatBot: thank you for chatting, Have a great day!")

if __name__ == "__main__":
    chat()  # Start the chat when the script is executed
