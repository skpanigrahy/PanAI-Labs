from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent.agent import run_agent

app = FastAPI(title="PanAI-Labs API", version="1.0.0")

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: list[Message]

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        response = run_agent([msg.dict() for msg in request.messages])
        return {"response": response}
    except Exception as e:
        error_msg = str(e)
        if "RESOURCE_EXHAUSTED" in error_msg:
            raise HTTPException(
                status_code=429, 
                detail="API quota exceeded. Please try again later or upgrade your plan."
            )
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/")
async def root():
    return {"message": "PanAI-Labs API is running"}