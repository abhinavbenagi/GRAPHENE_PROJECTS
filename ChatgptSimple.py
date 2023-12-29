import openai
from openai import OpenAI

client = OpenAI(api_key = "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")

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Give me 3 ideas for apps I could build with openai apis "}
  ]
)
print(response.choices[0].message.content)