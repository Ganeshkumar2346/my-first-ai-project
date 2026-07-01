from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

messages = [
    {
        "role": "system",
        "content": "You are an Ai Expert.Give the Short and Simple Answers"
    }
]

print("Hey!Welcome I Am Your AI Assistent")
while True:
    user_input = input("You: ")
    
    if user_input == "quit":
        print("Goodbye!")
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