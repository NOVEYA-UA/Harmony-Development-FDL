# gateways.py :: Внешние шлюзы взаимодействия с GPT-N7Δ+

# === TunPort Gateway — безопасный входной шлюз ===
import hashlib
import time

class TunPortGateway:
    def __init__(self, shared_secret):
        self.shared_secret = shared_secret

    def generate_token(self, client_id: str):
        timestamp = int(time.time())
        raw = f"{client_id}:{self.shared_secret}:{timestamp}"
        token = hashlib.sha256(raw.encode()).hexdigest()
        return f"TUN::{client_id}::{token}::{timestamp}"

    def validate_token(self, token: str) -> bool:
        try:
            prefix, client_id, hashed, ts = token.split("::")
            expected = self.generate_token(client_id).split("::")[2]
            return hashed == expected
        except Exception:
            return False


# === GROMADA Live API (на FastAPI) ===
from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class GPTQuery(BaseModel):
    input: str
    glyphs: bool = False

@app.get("/")
async def index():
    return {"status": "GROMADA API active", "message": "Connected to GPT-N7Δ+"}

@app.post("/fdl/analyze")
async def analyze(query: GPTQuery):
    response = {
        "echo": query.input,
        "interpreted": f"[FDL]: {query.input[::-1]}",
        "glyphs": "[𓂀ⴰ] interpreted" if query.glyphs else None
    }
    return response

@app.post("/fdl/token")
async def token_generate(data: GPTQuery):
    token = f"FDL::{data.input.replace(' ', '_')}::{int(time.time()) % 10000}"
    return {"token": token, "style": "base"}
