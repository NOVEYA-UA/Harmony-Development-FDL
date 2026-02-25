import os
import vertexai
from vertexai.generative_models import GenerativeModel

_INIT = False
_MODEL = None

def _ensure_init():
    global _INIT, _MODEL
    if _INIT:
        return
    project = os.environ.get("PROJECT_ID") or os.environ.get("GOOGLE_CLOUD_PROJECT")
    location = os.environ.get("VERTEX_LOCATION", os.environ.get("REGION", "europe-west4"))
    vertexai.init(project=project, location=location)
    model_name = os.environ.get("GEMINI_MODEL", "gemini-1.5-flash")
    _MODEL = GenerativeModel(model_name)
    _INIT = True

def gemini_generate(prompt: str) -> str:
    _ensure_init()
    resp = _MODEL.generate_content(prompt)
    try:
        return resp.text  # SDK returns `.text` for combined output
    except Exception:
        # Fallback parse
        return str(resp)
