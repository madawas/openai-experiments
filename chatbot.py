import openai
from dotenv import dotenv_values

config = dotenv_values('.env')

openai.api_key = config['API_KEY']

def chat(messages):
    print(f"Assistant: ", end="")
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
        print(content, end="", flush=True)
        complete_response += content
    print()
    return {"role": "assistant", "content": complete_response}

def main():
    print("Assistant: Hello! I'm a chatbot. How can I help you today?\n")

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