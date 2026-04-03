import os
from dotenv import load_dotenv
from services.llm import call_llm_gemini, call_llm_openai  # Assume you add OpenAI function

load_dotenv()

SYSTEM_PROMPT = "You are a helpful AI assistant."

def run_agent(messages):
    full_messages = [{"role": "system", "content": SYSTEM_PROMPT}] + messages
    
    # Try Gemini first
    try:
        return call_llm_gemini(full_messages)
    except Exception as e:
        if "RESOURCE_EXHAUSTED" in str(e):
            # Fallback to OpenAI
            return call_llm_openai(full_messages)
        raise