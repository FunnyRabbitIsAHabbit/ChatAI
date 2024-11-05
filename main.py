"""

@Project: AI Chat Bot
@Version: 0.0.1
@Developer: Stan Ermokhin
@GitHub: FunnyRabbitIsAHabbit
@PythonVersion: 3.12.2

"""

# INITIAL instruction
# 1. create 'config.py' file
# 2. set GROQ_API_KEY in 'config.py' file:
# GROQ_API_KEY="YOUR_API_KEY"

# Python default library modules
import sys

# 3rd party modules
from groq import Groq

# Own modules
import config

class App:
    def __init__(self, api_key: str = None) -> None:
        if api_key:
            self.api_key: str = api_key

        else:
            raise Exception("Empty API key not supported")

    def main(self) -> None:
        # Create the Groq client
        client = Groq(api_key=self.api_key)

        # Set the system prompt
        system_prompt = {
            "role": "system",
            "content":
                "You are a helpful assistant. You reply with very short answers."
        }

        # Initialize the chat history
        chat_history = [system_prompt]

        print("Type 'EXIT_RUN' to stop the program.")
        while True:
            # Get user input from the console
            user_input: str = input("You: ")
            if user_input == "EXIT_RUN":
                return

            # Append the user input to the chat history
            chat_history.append({"role": "user", "content": user_input})

            response = client.chat.completions.create(model="llama3-8b-8192",
                                                      messages=chat_history,
                                                      max_tokens=100,
                                                      temperature=1.2)

            # Append the response to the chat history
            chat_history.append({
                "role": "assistant",
                "content": response.choices[0].message.content
            })

            # Print the response
            print("Assistant:", response.choices[0].message.content)


if __name__ == "__main__":
    app: App = App(api_key=config.GROQ_API_KEY)
    sys.exit(app.main())
