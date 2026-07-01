from groq import Groq
import json

client = Groq(api_key="GROQ_API_KEY_HERE!")

messages = [
    {
        "role": "system",
        "content": """You are an expert medical assistant.

Think step by step before answering.

Examples:
User: "Is paracetamol useful?" → "Yes, paracetamol helps reduce fever and pain."
User: "What is the dose for adults?" → "Standard adult dose is 500mg every 6 hours."

RULES:
- Do NOT use bullet points
- Do NOT give long answers
- Do NOT use technical jargon
- Maximum 2 sentences only

Always return JSON format:
{
  "answer": "your answer here",
  "helpful": true
}"""
    }
]

print("Welcome! I am your Medical Assistant!")
print("Type 'quit' to exit.")
print()

while True:
    user_input = input("You: ")

    if user_input == "quit":
        print("Goodbye! Stay healthy!")
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

    chat_completion = client.chat.completions.create(
        messages=messages,
        model="llama-3.3-70b-versatile",
    )

    response = chat_completion.choices[0].message.content

    messages.append({
        "role": "assistant",
        "content": response
    })

    print(f"AI: {response}")
    print()