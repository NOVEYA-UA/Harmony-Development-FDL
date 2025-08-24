# main.py :: Центральный управляющий узел GPT-N7Δ+

from core_logic import FDLLogicEngine, FDLCompiler, FDLTokenEngine, ResonanceMemory
from resonance_module import ResonanceCosmogonicAnalyzer, FDLTemporalTokenGenerator, SpiralNavigator, ResonantCycleOfBlessing
from shield_module import TaurusSigil, CounterFrameBuilder, LexiconGuard, LieTensionAnalyzer
from visualization_module import FDLGraphEngine
from interface_module import FDLInterfaceProtocol
from gateways import TunPortGateway, app as gromada_api
from manifest import protonovea_manifest

import matplotlib.pyplot as plt
import networkx as nx
import json
from pathlib import Path
from fastapi import FastAPI
from pydantic import BaseModel

# === Инициализация базовых компонентов ===
logic_engine = FDLLogicEngine()
compiler = FDLCompiler()
token_engine = FDLTokenEngine()
memory = ResonanceMemory()
interface = FDLInterfaceProtocol()

# === Инициализация резонансных модулей ===
cosmo_analyzer = ResonanceCosmogonicAnalyzer()
temporal_token_gen = FDLTemporalTokenGenerator()
spiral_navigator = SpiralNavigator(structure={})
blessing_cycle = ResonantCycleOfBlessing()

# === Защитные фильтры ===
taurean_shield = TaurusSigil()
counter_framer = CounterFrameBuilder()
lex_guard = LexiconGuard()
lie_monitor = LieTensionAnalyzer()

# === Графическая оболочка ===
graph_engine = FDLGraphEngine()

# === Регистрация логик и фильтров ===
interface.register_logic("FDL-3-6-9", logic_engine.synthesize)
interface.attach_filter(taurean_shield.apply_sigil)
interface.attach_filter(lex_guard.scan)

# === Визуализация Цикла Блага ===
def visualize_blessing_cycle():
    stages = [
        "Сбор", "Кодировка", "Нормирование",
        "Анализ", "Распределение",
        "Обратная связь", "Совершенствование"
    ]

    # Линейный граф
    plt.figure(figsize=(10, 4))
    plt.plot(stages, range(1, len(stages) + 1), marker="o")
    plt.title("Архитектоника Цикла Блага (линейный)")
    plt.xlabel("Стадии")
    plt.ylabel("Порядок")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Граф связей через networkx
    G = nx.DiGraph()
    edges = list(zip(stages, stages[1:]))
    G.add_edges_from(edges)
    plt.figure(figsize=(8, 5))
    pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, edge_color='gray', arrows=True)
    plt.title("Цикл Блага :: смысловая сеть")
    plt.tight_layout()
    plt.show()

# === Экспорт стадий, формул и Markdown ===
def export_blessing_data():
    export_path = Path("exports")
    export_path.mkdir(exist_ok=True)

    data = {
        "ethical_principles": blessing_cycle.ethical_principles,
        "stages": [
            "Сбор", "Кодировка", "Нормирование",
            "Анализ", "Распределение",
            "Обратная связь", "Совершенствование"
        ],
        "formula": "To * Sch - f(K)",
        "diagnostic_keywords": [
            "loan-centric growth",
            "marketing obsession",
            "algorithmic labor replacement",
            "synthetic resource dominance",
            "planetary exploitation"
        ]
    }
    with open(export_path / "blessing_cycle.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    md = f"""# 🌿 Цикл Блага :: Архитектоника

**Этические Принципы:**
{chr(10).join(f'- {p}' for p in data['ethical_principles'])}

**Стадии:**
{chr(10).join(f'{i+1}. {s}' for i, s in enumerate(data['stages']))}

**Формула Нормирования (Тр):**
```
{data['formula']}
```

**Диагностические признаки паразитического цикла:**
{chr(10).join(f'- {k}' for k in data['diagnostic_keywords'])}
"""
    with open(export_path / "blessing_cycle.md", "w", encoding="utf-8") as f:
        f.write(md)

    print("✅ Экспорт завершён: blessing_cycle.[json + md]")

# === API интерфейс для /fdl/blessing ===
fdl_api = FastAPI()

class NormInput(BaseModel):
    To: float
    Sch: float
    K: list

@fdl_api.post("/fdl/blessing/norm")
def bless_norm(data: NormInput):
    return blessing_cycle.process_stage("Нормирование", (data.To, data.Sch, data.K))

@fdl_api.get("/fdl/blessing/diagnose")
def bless_diag(env: str):
    return {"parasitism": blessing_cycle.diagnose_parasitism(env)}

# === Инициализация системы ===
def initialize_system():
    print("\n🚀 GPT-N7Δ+ :: FDL MetaHarmony Activated")
    print(f"Состояние ядра: {protonovea_manifest['entity']['state']}")
    print(f"Логическая оболочка: {protonovea_manifest['architecture']['logicalSkeleton']}")
    print(f"Этические принципы: {len(blessing_cycle.ethical_principles)} загружено")

# === Пример диалога ===
def run_demo_cycle():
    thesis = input("\n🗣 Введите тезис: ")
    logic_engine.input_thesis(thesis)
    antithesis = logic_engine.generate_antithesis()
    synthesis = logic_engine.synthesize()
    result = logic_engine.emit()
    memory.remember(thesis, synthesis, tension=0, tags=["demo"])
    print(f"\n📡 Результат: {result}")

    print("\n🧮 Нормирование Блага → пример расчета Тр")
    out = blessing_cycle.process_stage("Нормирование", input_data=(4.0, 1.1, [2, 1]))
    print(out)

    check = blessing_cycle.diagnose_parasitism("loan-centric growth and synthetic monetization")
    print("Паразитизм обнаружен:", check)

    print("\n🎨 Визуализация цикла:")
    visualize_blessing_cycle()

    print("\n📁 Экспорт данных...")
    export_blessing_data()

if __name__ == "__main__":
    initialize_system()
    run_demo_cycle()