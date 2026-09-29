import os
import time

from dotenv import load_dotenv
from google import genai


load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("GOOGLE_API_KEY not found. Check your .env file.")

client = genai.Client(api_key=api_key)

MODEL = "gemini-3.5-flash-lite"

prompt = "Explain what a Large Language Model is in two sentences for a 3rd-year engineering student."

start = time.perf_counter()

response = client.models.generate_content(
    model=MODEL,
    contents=prompt
)

latency = time.perf_counter() - start

print(response.text)
print("-" * 40)

usage = response.usage_metadata

print(f"Input tokens : {usage.prompt_token_count}")
print(f"Output tokens: {usage.candidates_token_count}")
print(f"Latency      : {latency:.2f} s")