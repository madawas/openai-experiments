import openai
from dotenv import dotenv_values

config = dotenv_values('.env')

openai.api_key = config['API_KEY']

def completion(prompt, model='text-davinci-003', max_tokens=16, temperature=1, top_p=1.0, frequency_penalty=0.0, presence_penalty=0.0, n=1, echo=False):
    """
    Generates text using the OpenAI completion API.

    Parameters:
    - prompt (str): The input text to generate text from.
    - model (str): The model to use for text generation (default: 'text-davinci-003').
    - max_tokens (int): The maximum number of tokens in the generated response (default: 16).
    - temperature (float): Controls the randomness of the generated text (default: 1).
    - top_p (float): Nucleus sampling parameter to control diversity (default: 1.0).
    - frequency_penalty (float): Controls the penalty for repeating tokens (default: 0.0).
    - presence_penalty (float): Controls the penalty for including irrelevant tokens (default: 0.0).
    - n (int): Number of completions to generate. (default: 1)
    - echo (boolean): whether to include prompt in the completion (default: False)

    Returns:
    - completion (dict): API response
    """

    # Call the OpenAI API to generate text
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        n=n,
        echo=echo
    )

    return response

#Test basic prompt
prompt = "List the planets of the solar system in the order of the size"
response = completion(prompt=prompt, max_tokens=100)
print(response.choices[0].text.strip())

#Test prompt with n > 1.
# n = number of completions to generate
# When n > 1, max_token applies to each individual completion

prompt = "Tell me an interesting fact about OpenAI"
response = completion(prompt=prompt, max_tokens=100, n=3)
print(response.choices, response.usage)
