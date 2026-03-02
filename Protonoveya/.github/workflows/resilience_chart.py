import sqlite3
import math

def calculate_resilience():
    conn = sqlite3.connect("metatron_core.db")
    c = conn.cursor()
    
    # 1. Инфраструктура (I) - количество TRUST задач
    tasks_ok = c.execute("SELECT COUNT(*) FROM tasks WHERE audit_status='TRUST'").fetchone()[0]
    I = tasks_ok / 30.0
    
    # 2. Солидарность (S) - количество вкладов
    contribs = c.execute("SELECT COUNT(*) FROM contributions").fetchone()[0]
    S = math.log1p(contribs) # Логарифмический рост
    
    # 3. Энергия (E) - последняя когерентность
    energy = c.execute("SELECT coherence FROM energy_logs ORDER BY date DESC LIMIT 1").fetchone()
    E = (energy[0] / 100.0) if energy else 0.5
    
    # ФОРМУЛА НОВЕЯ: R = (I * E) + S
    resilience_score = (I * E) + S
    
    print("\n" + "="*40)
    print(f" ПОКАЗАТЕЛЬ СТОЙКОСТИ ГРОМАДИ: {resilience_score:.2f}")
    print("="*40)
    
    # Визуализация (ASCII-график)
    bar = "█" * int(resilience_score * 10)
    print(f"Resilience: {bar} {resilience_score:.2f}")
    
    if resilience_score > 1.5:
        print("\n[СТАТУС] СИСТЕМА В РЕЖИМЕ СОЗИДАНИЯ. НОВЕЯ АКТИВИРОВАНА.")
    
    conn.close()

if __name__ == "__main__":
    calculate_resilience()
