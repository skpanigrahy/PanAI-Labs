## ✅ API documentation ready

Since I can't create files directly, here's the complete content for your API guide. Create a new file at `g:\apps\PanAI-Labs\docs\API_GUIDE.md` and paste this in:

---

# PanAI-Labs API Guide

## Overview

FastAPI-based LLM service using Gemini (Google AI) with OpenAI fallback support.

## Setup

### Prerequisites

- Python 3.11+
- Virtual environment activated
- Dependencies installed: `pip install -r requirements.txt`

### Environment Variables

Create .env in project root:

```
GEMINI_API_KEY=your-gemini-api-key
OPENAI_API_KEY=your-openai-api-key  # Optional fallback
```

## Running the API

### Start Server

```bash
cd backend
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Access Points

- **API Docs**: http://localhost:8000/docs (Swagger UI)
- **Health Check**: http://localhost:8000/
- **Base URL**: http://localhost:8000

## API Endpoints

### GET /

Health check endpoint.

**Response:**

```json
{
  "message": "PanAI-Labs API is running"
}
```

### POST /chat

Send messages to LLM and get response.

**Request Body:**

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Hello, how are you?"
    }
  ]
}
```

**Response:**

```json
{
  "response": "I'm doing well, thank you for asking!"
}
```

**Error Response:**

```json
{
  "detail": "Error message here"
}
```

## Testing the API

### Using cURL

```bash
# Health check
curl http://localhost:8000/

# Chat request
curl -X POST "http://localhost:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {"role": "user", "content": "Hello from PanAI-Labs"}
    ]
  }'
```

### Using Python

```python
import requests

# Health check
response = requests.get("http://localhost:8000/")
print(response.json())

# Chat request
data = {
    "messages": [
        {"role": "user", "content": "Hello from PanAI-Labs"}
    ]
}
response = requests.post("http://localhost:8000/chat", json=data)
print(response.json())
```

### Using Swagger UI

1. Open http://localhost:8000/docs
2. Click on `POST /chat`
3. Click "Try it out"
4. Enter JSON in request body
5. Click "Execute"

## LLM Configuration

### Current Setup

- **Primary**: Gemini `models/gemini-2.0-flash-lite`
- **Fallback**: OpenAI GPT-4o-mini (if implemented)

### Quotas & Limits

- Gemini Free Tier: 60 req/min, 1M tokens/month
- Check usage: https://ai.google.dev/aistudio

## Troubleshooting

### Common Errors

- **429 RESOURCE_EXHAUSTED**: Quota exceeded, wait or upgrade
- **404 NOT_FOUND**: Invalid model name
- **500 Internal Server Error**: Check server logs

### Logs

Server logs appear in terminal. For production, configure logging.

## Development

### Project Structure

```
backend/
├── main.py          # FastAPI app
├── services/
│   └── llm.py       # LLM service
└── test_gemini.py   # Test script
```

### Adding Features

- Conversation history
- Streaming responses
- Multiple LLM providers
- Authentication

---
