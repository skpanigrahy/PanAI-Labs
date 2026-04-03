from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent.agent import run_agent
from agent.intent import analyze_intent
from agent.router import route_query
from agent.memory import memory

app = FastAPI(title="PanAI-Labs API", version="1.0.0")

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: list[Message]
    session_id: str = "default"

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        session_id = request.session_id
        messages = [msg.dict() for msg in request.messages]

        # Get last user query
        user_query = messages[-1]["content"]

        # Save user message
        memory.add_message(session_id, "user", user_query)

        # Get full history
        history = memory.get_history(session_id)

        # Intent detection
        intent = analyze_intent(user_query)

        # Route with history
        response = route_query(intent, history)

        # Save assistant response
        memory.add_message(session_id, "assistant", response)

        return {
            "intent": intent,
            "response": response,
            "history_length": len(history)
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@app.get("/")
async def root():
    return {"message": "PanAI-Labs API is running"}