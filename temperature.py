from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_ai(prompt, temperature):
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile",
        temperature=temperature,
    )
    return chat_completion.choices[0].message.content

# Run high temperature 3 times to see variation
print("HIGH TEMPERATURE - Run 1:")
print(ask_ai("Write a creative one-line slogan for a farming startup.", 1.0))
print()

print("HIGH TEMPERATURE - Run 2:")
print(ask_ai("Write a creative one-line slogan for a farming startup.", 1.0))
print()

print("HIGH TEMPERATURE - Run 3:")
print(ask_ai("Write a creative one-line slogan for a farming startup.", 1.0))