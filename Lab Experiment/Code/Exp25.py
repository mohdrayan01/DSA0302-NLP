# 25.Utilize the GPT-3 model to generate text based on a given prompt. Make sure to install the OpenAI GPT-3 library in python implementation.

from openai import OpenAI
# Replace with your OpenAI API key
client = OpenAI(api_key="your_api_key")
response = client.responses.create(
    model="gpt-4.1-mini",
    input="Write a short paragraph about Artificial Intelligence."
)
print(response.output_text)