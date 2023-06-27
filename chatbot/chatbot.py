import openai
import os
from dotenv import load_dotenv
from termcolor import colored

load_dotenv(dotenv_path="../.env")
openai.api_key = os.getenv("API_KEY")

def chat(messages):
    print(colored(f"\nAssistant: \n", "green"), end="")
    complete_response = ""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.8,
        stream=True
    )

    for chunk in response:
        if (not chunk.choices[0].delta):
            break
        content = chunk.choices[0].delta.content
        print(colored(content, "green"), end="", flush=True)
        complete_response += content
    print("\n")
    return {"role": "assistant", "content": complete_response}

def main():
    print(colored("Assistant: Hello! I'm a chatbot. How can I help you today?\n", "green"))

    messages = [{"role": "system", "content": "You are a helpful conversational chatbot"}]

    while True:
        try:
            prompt = input("You: ")
            messages.append({"role": "user", "content": prompt})
            messages.append(chat(messages))
        except KeyboardInterrupt:
            print("\n\nGood Bye!\n\n")
            break;

if __name__ == "__main__":
    main()