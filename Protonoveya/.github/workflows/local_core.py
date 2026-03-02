import os, sqlite3, requests, sys, re
from datetime import datetime
from pathlib import Path

# === CONFIGURATION ===
ASANA_PAT = os.getenv("ASANA_PAT", "").strip()
RAW_GID = os.getenv("ASANA_PROJECT_GID", "").strip()
PROJECT_GID = re.search(r'\d+', RAW_GID).group() if re.search(r'\d+', RAW_GID) else None

DB_PATH = Path("metatron_core.db")
SECTORS_DIR = Path("sectors")

def sync():
    if not ASANA_PAT or not PROJECT_GID:
        print(f"![Error] Данные не получены. PAT: {'OK' if ASANA_PAT else 'MISSING'}, GID: {PROJECT_GID}")
        return
    
    print(f"[{datetime.now()}] Синхронизация Metatron-8 v2.1...")
    headers = {"Authorization": f"Bearer {ASANA_PAT}"}
    url = f"https://app.asana.com/api/1.0/projects/{PROJECT_GID}/tasks?opt_fields=name,notes,gid"
    
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        tasks = r.json().get("data", [])
        
        conn = sqlite3.connect(DB_PATH)
        # Явное создание таблицы с 4 базовыми колонками (если её нет)
        conn.execute("CREATE TABLE IF NOT EXISTS tasks (id TEXT PRIMARY KEY, title TEXT, sector TEXT, level TEXT)")
        
        for t in tasks:
            name, gid, notes = t['name'], t['gid'], t.get('notes', '')
            lvl = "01_Logos" if "#Logos" in name else "03_Telos" if "#Telos" in name else "02_Nomos"
            
            sec = "00_Unsorted"
            for s in ["01","02","03","04","05","06","07","08"]:
                if s in name:
                    dirs = [d for d in os.listdir(SECTORS_DIR) if d.startswith(s)]
                    if dirs: sec = dirs[0]
                    break
            
            # ЯВНО указываем колонки, чтобы избежать ошибки table has X columns but Y values supplied
            conn.execute("INSERT OR REPLACE INTO tasks (id, title, sector, level) VALUES (?,?,?,?)", (gid, name, sec, lvl))
            
            path = SECTORS_DIR / sec / lvl
            path.mkdir(parents=True, exist_ok=True)
            with open(path / f"{gid}.md", "w", encoding="utf-8") as f:
                f.write(f"# {name}\n\n{notes}")
        
        conn.commit()
        conn.close()
        print(f"✓ Успех! Зафиксировано задач: {len(tasks)}")
    except Exception as e:
        print(f"![Error] Ошибка API: {e}")

if __name__ == "__main__":
    sync()
