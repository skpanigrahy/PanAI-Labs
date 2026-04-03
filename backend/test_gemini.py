import os
from dotenv import load_dotenv
import google.genai as genai

load_dotenv()  # Load .env file
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# List available models
print("Available models:")
models = client.models.list()
for model in models:
    print(f"- {model.name}")

def call_llm(messages):
    # Convert OpenAI-style messages → Gemini prompt
    prompt = ""
    for msg in messages:
        prompt += f"{msg['role']}: {msg['content']}\n"

    response = client.models.generate_content(
    model="models/gemini-2.0-flash-lite",  # Free tier model
    contents=prompt
    )
    return response.text

# Test it
if __name__ == "__main__":
    messages = [{"role": "user", "content": "Hello from PanAI-Labs"}]
    print("\nTesting LLM:")
    print(call_llm(messages))