
class RuleBasedChatbot:
    def __init__(self):
        self.rules = {
            "greeting": {
                "keywords": ["hi", "hello", "hey"],
                "response": "Hello! How can I help you today?"
            },
            "wellbeing": {
                "keywords": ["how are you", "how r you"],
                "response": "I'm doing well, thank you for asking."
            },
            "identity": {
                "keywords": ["your name", "who are you"],
                "response": "I am a rule-based chatbot developed using Python."
            },
            "help": {
                "keywords": ["help", "options"],
                "response": "You can greet me, ask about me, or type 'bye' to exit."
            },
            "exit": {
                "keywords": ["bye", "exit", "quit"],
                "response": "Goodbye! Have a great day."
            }
        }

    def preprocess_input(self, text):
        """
        Converts input text to lowercase and removes extra spaces.
        """
        return text.lower().strip()

    def find_response(self, user_input):
        """
        Matches user input against predefined rules
        and returns the corresponding response.
        """
        for rule in self.rules.values():
            for keyword in rule["keywords"]:
                if keyword in user_input:
                    return rule["response"]

        return "Sorry, I didn't understand that. Please try again."

    def start(self):
        """
        Starts the chatbot interaction loop.
        """
        print("Chatbot: Hello! I am ready to chat. Type 'bye' to exit.\n")

        while True:
            user_input = input("You: ")
            processed_input = self.preprocess_input(user_input)

            response = self.find_response(processed_input)
            print("Chatbot:", response)

            if processed_input in self.rules["exit"]["keywords"]:
                break


if __name__ == "__main__":
    chatbot = RuleBasedChatbot()
    chatbot.start()
