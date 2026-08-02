import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# API Keys
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Gemini Model
# Change this here if you want to use another model later.
GEMINI_MODEL = "models/gemini-3.5-flash"