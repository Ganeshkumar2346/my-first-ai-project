from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_ai(system_prompt, user_message):
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ],
        model="llama-3.3-70b-versatile",
    )
    return chat_completion.choices[0].message.content

# Combined prompt — all techniques together
response = ask_ai(
    """You are an expert customer support agent 
for an AI engineering course. (ROLE)

Think step by step before answering. (CHAIN OF THOUGHT)

Examples of good responses:
User: "Is this course free?" → "Yes, all materials are free!"
User: "How long is the course?" → "6 months of focused learning." (FEW SHOT)

RULES: (NEGATIVE PROMPTING)
- Do NOT use bullet points
- Do NOT give long answers
- Do NOT use technical jargon
- Maximum 2 sentences only

Always return JSON format: (JSON OUTPUT)
{
  "answer": "your answer here",
  "helpful": true
}""",

    "I am a beginner with no coding experience. Can I learn AI engineering?"
)

print("Combined Output:")
print(response)