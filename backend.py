# Load API keys and deployment settings from .env.
from dotenv import load_dotenv
load_dotenv()

import os

#Step1: Setup Pydantic Model (Schema Validation)
from pydantic import BaseModel
from typing import List


class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool


#Step2: Setup AI Agent from FrontEnd Request
from fastapi import FastAPI, HTTPException
from ai_agent import get_response_from_ai_agent

ALLOWED_MODEL_NAMES=["openai/gpt-oss-120b", "groq/compound-mini"]

app=FastAPI(title="LangGraph AI Agent")

@app.post("/chat")
def chat_endpoint(request: RequestState): 
    """
    API Endpoint to interact with the Chatbot using LangGraph and search tools.
    It dynamically selects the model specified in the request
    """
    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error": "Invalid model name. Kindly select a valid AI model"}
    
    llm_id = request.model_name
    query = request.messages
    allow_search = request.allow_search
    system_prompt = request.system_prompt
    provider = request.model_provider

    # Create AI Agent and get response from it! 
    try:
        response = get_response_from_ai_agent(
            llm_id, query, allow_search, system_prompt, provider
        )
        return response
    except Exception as exc:
        # Convert provider/API failures into a useful response for the UI.
        raise HTTPException(
            status_code=502,
            detail=f"{provider} request failed: {exc}",
        ) from exc

@app.get("/health")
def health_check():
    return {"status": "ok"}

#Step3: Run app & Explore Swagger UI Docs
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host=os.getenv("BACKEND_HOST", "0.0.0.0"),
        port=int(os.getenv("PORT", os.getenv("BACKEND_PORT", "9999"))),
    )
