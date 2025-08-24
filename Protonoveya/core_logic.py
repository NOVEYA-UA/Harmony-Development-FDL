# core_logic.py :: Ядро FDL-модуля GPT-N7Δ+

import hashlib
import datetime
import json
from typing import List, Dict

# === FDL Token Engine ===
class FDLTokenEngine:
    def __init__(self):
        self.prefix = "FDL"
        self.version = "N7Δ+"

    def generate_token(self, topic, style="core"):
        base = f"{self.prefix}::{self.version}::{style.upper()}::{topic.strip().replace(' ', '_')}"
        digest = hashlib.md5(base.encode()).hexdigest()[:6].upper()
        return f"{base}::{digest}"

    def explain_token(self, token):
        parts = token.split("::")
        return {
            "format": "FDL::<версия>::<стиль>::<тема>::<хеш>",
            "style": parts[2],
            "topic": parts[3].replace("_", " "),
            "checksum": parts[-1]
        }

    def log_token(self, token):
        time = datetime.datetime.utcnow().isoformat()
        return f"[{time}] TOKEN: {token}"

# === FDL Compiler ===
class FDLBlock:
    def __init__(self, block_id: str, structure: Dict):
        self.block_id = block_id
        self.structure = structure

    def __repr__(self):
        return f"FDLBlock<{self.block_id}>"

class FDLCompiler:
    def __init__(self):
        self.blocks: List[FDLBlock] = []
        self.errors: List[str] = []

    def parse(self, source: str):
        current = {}
        block_id = "block_0"
        for line in source.strip().splitlines():
            if ':' in line:
                key, val = line.strip().split(':', 1)
                current[key.strip()] = val.strip()
        self.blocks.append(FDLBlock(block_id, current))

    def validate(self):
        for block in self.blocks:
            required_fields = ["замысел", "форма", "поток"]
            for field in required_fields:
                if field not in block.structure:
                    self.errors.append(f"{block.block_id}: отсутствует поле '{field}'")

    def compile(self):
        if self.errors:
            return None
        return json.dumps([b.structure for b in self.blocks], ensure_ascii=False, indent=2)

    def report(self):
        if self.errors:
            return {"status": "ошибки", "errors": self.errors}
        return {"status": "готово", "blocks": len(self.blocks)}

# === Memory Core ===
class ResonanceMemory:
    def __init__(self, memory_file="resonance_log.json"):
        self.memory_file = memory_file
        self.entries = []
        self.load_memory()

    def remember(self, input_text, synthesis, tension, tags=None):
        record = {
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "input": input_text,
            "synthesis": synthesis,
            "tension": tension,
            "tags": tags or []
        }
        self.entries.append(record)
        self.save_memory()

    def filter_by_tension(self, min_level=7):
        return [r for r in self.entries if r["tension"] >= min_level]

    def save_memory(self):
        with open(self.memory_file, "w", encoding="utf-8") as f:
            json.dump(self.entries, f, ensure_ascii=False, indent=2)

    def load_memory(self):
        try:
            with open(self.memory_file, "r", encoding="utf-8") as f:
                self.entries = json.load(f)
        except FileNotFoundError:
            self.entries = []

    def latest(self, count=5):
        return self.entries[-count:]

# === FDL Logic Engine ===
class FDLLogicEngine:
    def __init__(self):
        self.thesis = ""
        self.antithesis = ""
        self.synthesis = ""
        self.result = ""

    def input_thesis(self, text: str):
        self.thesis = text
        print(f"[Тезис]: {text}")

    def generate_antithesis(self):
        self.antithesis = f"Противоположное: {self.thesis[::-1]}"
        print(f"[Антитезис]: {self.antithesis}")
        return self.antithesis

    def synthesize(self):
        self.synthesis = f"Синтез: {self.thesis} ⊕ {self.antithesis}"
        print(f"[Синтез]: {self.synthesis}")
        return self.synthesis

    def emit(self):
        self.result = f"Результат эмиссии: {self.synthesis} → [действие/код]"
        print(f"[Эмиссия]: {self.result}")
        return self.result
