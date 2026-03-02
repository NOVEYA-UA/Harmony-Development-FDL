import zipfile
import os
from datetime import datetime
from pathlib import Path

def pack_ark():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    ark_name = f"NOVEYA_ARK_SIGMA_{timestamp}.zip"
    base_path = Path(".")
    
    print(f"--- ЗАПУСК ПРОТОКОЛА 'КОВЧЕГ' ({ark_name}) ---")
    
    with zipfile.ZipFile(ark_name, 'w', zipfile.ZIP_DEFLATED) as ark:
        for root, dirs, files in os.walk(base_path):
            # Пропускаем сам архив и скрытые папки git
            if ark_name in files or ".git" in root:
                continue
            for file in files:
                file_path = Path(root) / file
                ark.write(file_path, file_path.relative_to(base_path))
                
    print(f"✓ Ковчег сформирован: {os.path.abspath(ark_name)}")
    print(f"Размер: {os.path.getsize(ark_name) / 1024:.2f} KB")
    print("--- СИСТЕМА ГОТОВА К ПЕРЕДАЧЕ ---")

if __name__ == "__main__":
    pack_ark()
