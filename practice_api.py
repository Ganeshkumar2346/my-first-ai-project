from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_ai(system_prompt, user_input):
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ],
        model="llama-3.3-70b-versatile",
    )

    return chat_completion.choices[0].message.content


response1 = ask_ai(
    "You are a helpful assistant.",
    "What is machine learning?"
)

print("BASIC ROLE:")
print(response1)
print()

response2 = ask_ai(
    "You are an AI engineering expert who explains everything in simple 2-3 lines only. No long answers ever.",
    "What is machine learning?"
)

print("SPECIFIC ROLE:")
print(response2)