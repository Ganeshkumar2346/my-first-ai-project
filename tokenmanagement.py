from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

chat_completion = client.chat.completions.create(
    messages=[{"role": "user", "content": "What is AI in one line?"}],
    model="llama-3.3-70b-versatile",
    max_tokens=50,
)

print(chat_completion.choices[0].message.content)
print()
print("Tokens used:", chat_completion.usage.total_tokens)
print("Prompt tokens:", chat_completion.usage.prompt_tokens)
print("Response tokens:", chat_completion.usage.completion_tokens)