import os
from dotenv import load_dotenv

load_dotenv()

LLM_PROVIDER = os.getenv("LLM_PROVIDER", "mock")  
# options: gemini | openai | mock


# ---------------- MOCK ----------------
def mock_llm(messages):
    last_user = [m for m in messages if m["role"] == "user"][-1]["content"]

    # Simple memory simulation
    history_text = " ".join(m["content"] for m in messages)

    if "my name is" in history_text.lower():
        name = history_text.lower().split("my name is")[-1].strip().split()[0]

        if "what is my name" in last_user.lower():
            return f"[MOCK MEMORY] Your name is {name.capitalize()}"

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