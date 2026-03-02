import os
import sqlite3
from pathlib import Path

# === CONFIGURATION ===
DB_PATH = Path("metatron_core.db")
SECTORS_DIR = Path("sectors")

# Ключевые слова "паразитарного шума" (Сектор 06)
RISK_MARKERS = {
    "rotary": "Внешнее влияние (клубная структура)",
    "grant": "Финансовая зависимость (гранты)",
    "ebsc": "Корпоративное давление (EBSC)",
    "usaid": "Геополитический шум (USAID)",
    "ebrd": "Кредитное обременение (EBRD)",
    "opaque": "Непрозрачность процессов",
    "centralized": "Риск централизации"
}

def run_audit():
    print("--- ЗАПУСК CII-AUDIT (Metatron-8) ---")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Ищем все .md файлы в секторах
    for md_file in SECTORS_DIR.glob("**/*.md"):
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read().lower()
        
        found_risks = []
        for marker, description in RISK_MARKERS.items():
            if marker in content:
                found_risks.append(f"{marker.upper()}")

        # Определяем статус
        status = "RISK" if found_risks else "TRUST"
        gid = md_file.stem # имя файла - это GID задачи

        # Обновляем БД (добавим колонку статуса, если нет)
        try:
            cursor.execute("ALTER TABLE tasks ADD COLUMN audit_status TEXT")
        except:
            pass
        
        cursor.execute("UPDATE tasks SET audit_status = ? WHERE id = ?", (status, gid))
        
        # Обновляем сам файл (добавляем метку аудита в начало)
        if f"AUDIT: {status}" not in content.upper():
            with open(md_file, "r+", encoding="utf-8") as f:
                original = f.read()
                f.seek(0, 0)
                f.write(f"--- [CII-AUDIT: {status}] ---\n--- [MARKERS: {', '.join(found_risks) if found_risks else 'NONE'}] ---\n\n" + original)

        print(f"[*] Файл {md_file.name}: [{status}]")

    conn.commit()
    conn.close()
    print("--- АУДИТ ЗАВЕРШЕН. ИММУНИТЕТ ОБНОВЛЕН ---")

if __name__ == "__main__":
    run_audit()
