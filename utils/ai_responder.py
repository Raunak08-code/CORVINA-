import os
from dotenv import load_dotenv
from openai import OpenAI


# FORCE loading .env from project root
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

# THIS LINE IS CRITICAL
#load_dotenv()venv\venv|

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
You are CORVINA, an intelligent and professional email assistant.
Be polite, concise, and helpful.
"""

def generate_ai_reply(user_message: str) -> str:
        return f"CORVINA (mock reply): I understand your issue — we’ll get back to you shortly."

    # response = client.chat.completions.create(
    #     model="gpt-4o-mini",
    #     messages=[
    #         {"role": "system", "content": SYSTEM_PROMPT},
    #         {"role": "user", "content": user_message}
    #     ],
    #     temperature=0.3,
    #     max_tokens=200
    # )
    # return response.choices[0].message.content.strip()
