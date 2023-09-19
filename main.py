# Import OpenAI Python Library (https://github.com/openai/openai-python)
import openai

# Import Config file
import config

openai.api_key = config.api_key

print("CHATGPT with Python")
print("Type Exit to finish the program")

# Assistent Context setup
messages = [{"role": "system", "content": "You are an skilled developer"}]

while True:

    content = input("What do you want to talk about? ")

    if content == "Exit":
        break

    messages.append({"role": "user", "content": content})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages)
    
    response_content = response.choices[0].message.content

    messages.append({"role": "assistant", "content": response_content})

    print(response_content)
