import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
MODEL = "gemini-3.5-flash-lite"

samples = [
    "Goutham Aduri",
    "Kongu Engineering College",
    "கொங்கு பொறியியல் கல்லூரி",
    "The fan in room 214 is not working since three days.",
    'def greet(name):\n    return f"Hello, {name}!"',
]
for text in samples:
    result = client.models.count_tokens(model=MODEL, contents=text)
    words = len(text.split())
    print(f"{result.total_tokens:>4} tokens | {words:>2} words | {text}")