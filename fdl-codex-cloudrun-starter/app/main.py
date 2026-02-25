import base64
import os
from typing import Optional

from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel, Field

from .vertex_client import gemini_generate

APP_NAME = os.environ.get("APP_NAME", "fdl-codex")
PROJECT_ID = os.environ.get("PROJECT_ID", "")
LOCATION = os.environ.get("VERTEX_LOCATION", os.environ.get("REGION", "europe-west4"))

app = FastAPI(title="Σ-FDL-CODEX Orchestrator", version="0.1.0")

class TryIn(BaseModel):
    query: str = Field(..., description="Prompt for Gemini")

class TryOut(BaseModel):
    output: str

@app.get("/health")
async def health():
    return {"status": "ok", "app": APP_NAME, "project": PROJECT_ID, "location": LOCATION}

@app.post("/try", response_model=TryOut)
async def try_it(body: TryIn):
    text = gemini_generate(body.query)
    return TryOut(output=text)

# -- Pub/Sub push endpoint
class PubSubMessage(BaseModel):
    message: dict
    subscription: Optional[str] = None

@app.post("/pubsub/push")
async def pubsub_push(payload: PubSubMessage, request: Request):
    # Optional: verify OIDC token audience
    expected_aud = os.environ.get("PUBSUB_AUDIENCE")
    if expected_aud:
        # In Cloud Run, auth is enforced by platform; if you want extra checks, add here
        pass

    msg = payload.message or {}
    data_b64 = msg.get("data")
    if not data_b64:
        raise HTTPException(status_code=400, detail="Missing message.data")
    try:
        raw = base64.b64decode(data_b64).decode("utf-8")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Bad base64: {e}")
    # For demo, just echo
    return {"received": raw}
