import os
from dotenv import load_dotenv

load_dotenv()

LLM_PROVIDER = os.getenv("LLM_PROVIDER", "mock")  
# options: gemini | openai | mock


# ---------------- MOCK ----------------
def mock_llm(messages):
    last_user = messages[-1]["content"]

    if "Context:" in last_user:
        context_part = last_user.split("Context:")[1].split("Question:")[0].strip()
        question = last_user.split("Question:")[-1].strip()

        return f"[MOCK RAG] Based on context: {context_part}"

    return f"[MOCK RESPONSE] You asked: '{last_user}'"


# ---------------- GEMINI ----------------
def gemini_llm(messages):
    import google.genai as genai

    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    prompt = "\n".join(f"{msg['role']}: {msg['content']}" for msg in messages)

    response = client.models.generate_content(
        model="models/gemini-2.0-flash-lite",
        contents=prompt
    )

    return response.text


# ---------------- OPENAI ----------------
def openai_llm(messages):
    from openai import OpenAI

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    return response.choices[0].message.content


# ---------------- MAIN ----------------
def call_llm(messages):
    if LLM_PROVIDER == "gemini":
        return gemini_llm(messages)

    elif LLM_PROVIDER == "openai":
        return openai_llm(messages)

    else:
        return mock_llm(messages)