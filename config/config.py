from dotenv import load_dotenv
import os

load_dotenv()

# Email credentials
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")

# OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

