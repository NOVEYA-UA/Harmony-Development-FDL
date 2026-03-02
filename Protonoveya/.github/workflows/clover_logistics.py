import json, sqlite3
from pathlib import Path
from datetime import datetime

# === CONFIGURATION ===
DB_PATH = Path("metatron_core.db")
DATA_PATH = Path("sectors/04_Food/02_Nomos/village_resources.json")

NODES = ["Novosafronovka", "Podolyanka", "Snegirevka", "Mykolaiv_Sigma"]

def init_logistics():
    if not DATA_PATH.exists():
        initial_map = {
            "Novosafronovka": {"resources": ["Seeds", "Milk"], "needs": ["Energy", "Legal_Aid"]},
            "Podolyanka": {"resources": ["Grain", "Honey"], "needs": ["Water_Filters", "Tools"]},
            "Snegirevka": {"resources": ["Vegetables"], "needs": ["Seeds", "Medical_Supplies"]}
        }
        DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
        with open(DATA_PATH, "w", encoding="utf-8") as f:
            json.dump(initial_map, f, indent=4, ensure_ascii=False)
        print(f"[*] Логистическая карта создана: {DATA_PATH}")

def sync_logistics():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        nodes_data = json.load(f)
    
    conn = sqlite3.connect(DB_PATH)
    conn.execute("CREATE TABLE IF NOT EXISTS logistics (node TEXT PRIMARY KEY, has TEXT, wants TEXT)")
    
    print("--- СИНХРОНИЗАЦИЯ УЗЛОВ «КЛИНА» (Sector 04) ---")
    for node, info in nodes_data.items():
        conn.execute("INSERT OR REPLACE INTO logistics VALUES (?,?,?)",
                     (node, ", ".join(info['resources']), ", ".join(info['needs'])))
        print(f"[+] Узел {node}: Ресурсы [{info['resources']}] -> Потребности [{info['needs']}]")
    
    conn.commit()
    conn.close()
    print("--- СЕТЬ СИНХРОНИЗИРОВАНА ---")

if __name__ == "__main__":
    init_logistics()
    sync_logistics()
