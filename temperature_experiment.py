import csv
import os
import time
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
MODEL = "gemini-3.5-flash-lite"
PROMPT = "Suggest a name for our college tech fest. Reply with only the name."

rows = []
for temperature in [0.0, 0.7, 1.5]:
    for run in range(1, 4):
        start = time.perf_counter()
        response = client.models.generate_content(
            model=MODEL,
            contents=PROMPT,
            config=types.GenerateContentConfig(temperature=temperature),
        )
        latency = time.perf_counter() - start
        usage = response.usage_metadata
        name = response.text.strip()
        rows.append([temperature, run, name, usage.prompt_token_count,
                     usage.candidates_token_count, round(latency, 2)])
        print(f"T={temperature:<4} run {run}: {name}  ({latency:.2f}s)")
        time.sleep(2)   # stay inside free-tier rate limits

with open("temperature_results.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["temperature", "run", "output", "input_tokens", "output_tokens", "latency_s"])
    writer.writerows(rows)
print("Saved temperature_results.csv")