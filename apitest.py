import openai
from dotenv import dotenv_values

config = dotenv_values('.env')

openai.api_key = config['API_KEY']

response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Most famous book is "
)

print(response)