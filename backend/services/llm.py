import os
from dotenv import load_dotenv
import google.genai as genai
import openai

load_dotenv()

# Gemini client
gemini_client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# OpenAI client
openai.api_key = os.getenv("OPENAI_API_KEY")

def call_llm_gemini(messages):
    """Call Gemini API"""
    prompt = "\n".join(f"{msg['role']}: {msg['content']}" for msg in messages)
    
    response = gemini_client.models.generate_content(
        model="models/gemini-2.0-flash-lite",
        contents=prompt
    )
    
    return response.text

def call_llm_openai(messages):
    """Call OpenAI API"""
    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=1000
        )
        return response.choices[0].message.content
    except Exception as e:
        raise Exception(f"OpenAI error: {str(e)}")