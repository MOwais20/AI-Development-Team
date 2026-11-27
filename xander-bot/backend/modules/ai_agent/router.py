import logging

from fastapi import APIRouter, HTTPException
from langgraph.errors import GraphRecursionError
from openai import APIError, OpenAIError
from .schema import chat_payload
from . import service
from middlewares.authenticate import api_authenticate_key


ai_agent_router = APIRouter(prefix="/ai")
log = logging.getLogger(__name__)



@ai_agent_router.post("/chat")
def initiate_chat(payload: chat_payload):
    try:
        answer = service.chat(payload.query, payload.session_id)
    except (APIError, GraphRecursionError):   # first: both subclass the types below
        log.exception("Chat failed at the model")
        raise HTTPException(502, "The assistant couldn't complete this request.")
    except (OpenAIError, RuntimeError):
        log.exception("Chat model is not available")
        raise HTTPException(503, "The assistant is not available.")
    return {"session_id": payload.session_id, "answer": answer}

@ai_agent_router.get("/history")
def get_history(session_id: str):
    return {
        "session_id": session_id, 
        "messages": service.get_history(session_id)
    }
