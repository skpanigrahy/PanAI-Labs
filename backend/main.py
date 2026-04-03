from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent.agent import run_agent
from agent.intent import analyze_intent
from agent.router import route_query

app = FastAPI(title="PanAI-Labs API", version="1.0.0")

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: list[Message]

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        messages = [msg.dict() for msg in request.messages]

        # Extract latest user query
        user_query = messages[-1]["content"]

        # Step 1: Intent detection
        intent = analyze_intent(user_query)

        # Step 2: Routing
        response = route_query(intent, messages)

        return {
            "intent": intent,
            "response": response
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@app.get("/")
async def root():
    return {"message": "PanAI-Labs API is running"}