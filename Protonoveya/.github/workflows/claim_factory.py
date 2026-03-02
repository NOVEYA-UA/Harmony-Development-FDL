import os, json
from pathlib import Path

T_PATH = Path("sectors/12_Legal/02_Nomos/CLAIM_TEMPLATE_V1.md")
D_PATH = Path("sectors/05_Economy/02_Nomos/claims_data.json")
O_DIR = Path("sectors/05_Economy/03_Telos/GENERATED_CLAIMS")

def generate():
    if not D_PATH.exists():
        data = [{"name": "Тест Тестович", "address": "ул. Соборная, 1", "provider": "Николаевводоканал", "period": "январь 2026"}]
        with open(D_PATH, "w", encoding="utf-8") as f: json.dump(data, f, indent=4, ensure_ascii=False)
        return
    O_DIR.mkdir(parents=True, exist_ok=True)
    with open(T_PATH, "r", encoding="utf-8") as f: temp = f.read()
    with open(D_PATH, "r", encoding="utf-8") as f: residents = json.load(f)
    for p in residents:
        c = temp.replace("[Найменування споживача / адреса]", f"{p['name']}, {p['address']}")
        c = c.replace("[Найменування постачальника]", p['provider'])
        c = c.replace("[Период]", p['period'])
        with open(O_DIR / f"CLAIM_{p['name'].replace(' ', '_')}.md", "w", encoding="utf-8") as f: f.write(c)
        print(f"[+] Сгенерировано: {p['name']}")

if __name__ == "__main__":
    generate()
