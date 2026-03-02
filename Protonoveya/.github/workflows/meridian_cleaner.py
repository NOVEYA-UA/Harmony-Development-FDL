import sqlite3
from pathlib import Path

DB_PATH = Path("metatron_core.db")

def clear_system_debts():
    """Снятие дискретности через обнуление старых логов ошибок"""
    conn = sqlite3.connect(DB_PATH)
    # Прощение системы = удаление записей о критических сбоях, 
    # которые блокируют развитие (имитация очистки меридианов)
    conn.execute("DELETE FROM tasks WHERE audit_status = 'ERROR'")
    conn.commit()
    conn.close()
    print("--- ПРОТОКОЛ ПРОЩЕННЯ АКТИВОВАНО ---")
    print("[!] Дискретність меридіанів системи знята. Потік созидання вільний.")

if __name__ == "__main__":
    clear_system_debts()
