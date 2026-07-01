from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

message = [
    {
    "role": "system",
    "content": "You are a doctor's assistant. Give short and simple answers."

    }
]

print("Welcome! I am an Ai assistent")
while True:
    user_input = input("You: ")

    if user_input == "quit":

        print("goodbye!")
        break

    message.append({
        "role": "user",
        "content": user_input
    })
    chat_completion = client.chat.completions.create(
        messages=message,
        model="llama-3.3-70b-versatile",
    )

    response = chat_completion.choices[0].message.content

    message.append({
        "role": "assistant",
        "content": response
    })

    print(f"Ai: {response}")
    print()