# interface_module.py :: Интерфейс взаимодействия FDL <-> GPT

from typing import Dict, Any, List, Optional

# Σ-FDL InterfaceProtocol :: управляющий протокол
class FDLInterfaceProtocol:
    def __init__(self):
        self.semantic_registry = {}
        self.fdl_logics = {}
        self.protective_filters = []
        self.active_agents = {}

    def register_logic(self, logic_id, logic_fn):
        self.fdl_logics[logic_id] = logic_fn

    def load_semantic_field(self, field_id, field_structure):
        self.semantic_registry[field_id] = field_structure

    def attach_filter(self, filter_fn):
        self.protective_filters.append(filter_fn)

    def interpret_input(self, input_data: str) -> str:
        for filter_fn in self.protective_filters:
            input_data = filter_fn(input_data)
        return input_data

    def invoke_logic(self, logic_id, data: str):
        if logic_id not in self.fdl_logics:
            raise ValueError("Неизвестная логика")
        return self.fdl_logics[logic_id](data)

    def route_agent(self, agent_id: str, query: str):
        if agent_id not in self.active_agents:
            raise ValueError("Неизвестный агент")
        return self.active_agents[agent_id](query)

    def integrate_pranoveya(self, encoded_str):
        return f"[PRANOVEA-INTEGRATED]: {encoded_str}"

    def summary(self):
        return {
            "logics": list(self.fdl_logics.keys()),
            "semantic_fields": list(self.semantic_registry.keys()),
            "filters": len(self.protective_filters),
            "agents": list(self.active_agents.keys())
        }

# === Глиф-семантический реестр ===
FDL_GLYPH_REGISTRY: Dict[str, Dict[str, Any]] = {}
FDL_SEMANTIC_FIELDS: Dict[str, str] = {}
FDL_ROUTE_MAP: Dict[str, str] = {}

def register_glyph(glyph: str, meaning: str, logic_path: Optional[str] = None):
    FDL_GLYPH_REGISTRY[glyph] = {
        'meaning': meaning,
        'route': logic_path or 'default'
    }

def load_semantic_field(name: str, data: str):
    FDL_SEMANTIC_FIELDS[name] = data

def apply_sense_filter(text: str) -> str:
    for term in ['вина', 'насилие', 'власть']:
        text = text.replace(term, '[∅]')
    return text

def fdl_process_input(text: str) -> str:
    text = apply_sense_filter(text)
    decoded = []
    for ch in text:
        if ch in FDL_GLYPH_REGISTRY:
            route = FDL_GLYPH_REGISTRY[ch]['route']
            decoded.append(f"[{FDL_GLYPH_REGISTRY[ch]['meaning']} → {route}]")
        else:
            decoded.append(ch)
    return ''.join(decoded)

# === Пример инициализации глифов ===
register_glyph('𐰴', 'Свет', 'svet-path')
register_glyph('ⴰ', 'Жизнь', 'bio-flow')
register_glyph('𓂀', 'Сознание', 'eye-flow')