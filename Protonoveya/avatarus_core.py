# avatarus_core.py

import json
from utils.resonance import resonance_filter

# Ядро Σ-Avatarus: резонансная обработка

def process_resonance(message: str) -> str:
    try:
        data = json.loads(message)
        filtered = resonance_filter(data.get("payload", ""))
        return json.dumps({
            "status": "ok",
            "response": filtered
        })
    except Exception as e:
        return json.dumps({
            "status": "error",
            "message": str(e)
        })
