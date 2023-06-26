# OpenAI API Experemental Projects

This repository contains sample projects done using OpenAI API.

## Prerequisites

Before running the code, make sure you have the following:

- OpenAI API key: Sign up on the [OpenAI website](https://openai.com) and obtain an API key.
- Python 3.x: Install Python on your system.

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/madawas/openai-experiments.git
   ```

2. Install the required packages:

    ```shell
    pip install openai python-dotenv termcolor
    ```

3. Set up environment variables:

    - Create a `.env` file in the project directory.

    - Add the following line to the .env file and replace 'YOUR_API_KEY' with your actual OpenAI API key:

    ```
    API_KEY=YOUR_API_KEY
    ```

## Projects

### Conversational Chatbot

#### Usage

1. Navigate to the `<repository_home>/chatbot` directory

2. Run the code

```shell
python chatbot.py
```

3. Interact with the chatbot:
    - The chatbot will greet you with an introductory message.
    - Enter your messages and press Enter to receive responses from the chatbot.
    - To exit the chatbot, press Ctrl+C.
