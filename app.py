import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

print("Reading input text...")
with open("input.txt", "r", encoding="utf-8") as file:
    raw_text = file.read()

print("Sending to DeepSeek for translation and summarization...")
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a translator. Translate the provided Japanese text to English and add a brief 3-bullet-point summary at the top."},
        {"role": "user", "content": raw_text}
    ]
)

output_text = response.choices[0].message.content

print("Saving results...")
with open("output.txt", "w", encoding="utf-8") as file:
    file.write(output_text)

print("Process complete! Check output.txt.")