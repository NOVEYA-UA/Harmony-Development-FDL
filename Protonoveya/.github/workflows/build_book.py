import os
from pathlib import Path
from datetime import datetime

# Шляхи до ключових артефактів
DOCS = [
    "sectors/07_Culture/01_Logos/MANIFEST_SOVEREIGNTY.md",
    "sectors/01_Governance/01_Logos/SUBJECTIVITY_ACT.md",
    "sectors/02_Energy/01_Logos/BIO_NORM_REGLAMENT.md",
    "sectors/06_Security/01_Logos/NMPP_SHIELD_CONCEPT.md",
    "sectors/03_Water/02_Nomos/BORISENKO_SPEC.md",
    "sectors/08_Tech/01_Logos/CHILDHOOD_MANIFEST.md"
]

BOOK_PATH = Path("sectors/07_Culture/03_Telos/SVOD_NOVEYA_2026.md")

def build():
    print("--- ЗБІРКА ЗВОДУ НОВЕЯ (Синтез) ---")
    content = f"# ЗВІД НОВЕЯ: ТЕЛОС ГРОМАДИ\n"
    content += f"*Сформовано Узлом Sigma: {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n\n"
    content += "--- \n\n"

    for doc_path in DOCS:
        path = Path(doc_path)
        if path.exists():
            with open(path, "r", encoding="utf-8") as f:
                content += f.read() + "\n\n---\n\n"
            print(f"[+] Інтегровано: {path.name}")
        else:
            print(f"[!] Пропущено (не знайдено): {path.name}")

    with open(BOOK_PATH, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"--- ГОТОВО: {BOOK_PATH} ---")

if __name__ == "__main__":
    build()
