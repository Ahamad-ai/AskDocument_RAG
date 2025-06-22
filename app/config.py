import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
OPENAI_API_KEY = os.getenv("OPEN_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("🚨 GROQ_API_KEY is not set in the .env file.")

if not OPENAI_API_KEY:
    raise ValueError("🚨 OPEN_API_KEY is not set in the .env file.")