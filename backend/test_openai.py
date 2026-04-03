import os
from dotenv import load_dotenv
import openai

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise SystemExit("OPENAI_API_KEY not found")
openai.api_key = api_key

print("Using OPENAI_API_KEY:", api_key[:8] + "..." if api_key else None)

# New client API - access .data and use attributes
resp = openai.models.list()
print("Model count:", len(resp.data))
print("First model:", resp.data[0].id)

resp = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role":"user","content":"Hello from PanAI-Labs"}],
    max_tokens=50,
)
print(resp.choices[0].message.content)