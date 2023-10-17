# Import OpenAI Python Library (https://github.com/openai/openai-python)
import openai

# Import Config file
import config

openai.api_key = config.api_key

# Generating Chat 
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Who are you?"}])
print(response)
