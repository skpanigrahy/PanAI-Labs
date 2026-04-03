import os
from dotenv import load_dotenv
from services.llm import call_llm

load_dotenv()

SYSTEM_PROMPT = "You are a helpful AI assistant."

def run_agent(messages):
    full_messages = [{"role": "system", "content": SYSTEM_PROMPT}] + messages

    response = call_llm(full_messages)

    return response