import sqlite3
conn = sqlite3.connect("metatron_core.db")
res = conn.execute("SELECT audit_status, COUNT(*) FROM tasks GROUP BY audit_status").fetchall()
print("\n--- РЕЗОНАНС СИСТЕМЫ METATRON-8 ---")
for status, count in res:
    print(f"Статус {status if status else 'PENDING'}: {count} задач")
print("----------------------------------\n")
