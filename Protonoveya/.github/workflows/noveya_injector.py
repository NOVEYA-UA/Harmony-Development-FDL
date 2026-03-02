import os

def collect_project_knowledge(directory=r"C:\СОЦИАЛЬНЫЙ ПРОЕКТ НОВЕЯ"):
    knowledge_base = ""
    print(f"Σ-FDL :: СЕКТОР 11 :: Поглощение данных из {directory}...")
    
    if not os.path.exists(directory): return ""

    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)
            content = ""
            # Цикл обхода кодировок (UTF-8 -> Windows-1251 -> Latin-1)
            for enc in ['utf-8', 'windows-1251', 'latin-1']:
                try:
                    with open(filepath, 'r', encoding=enc) as f:
                        content = f.read()
                    print(f" -> {filename} (кодировка: {enc})")
                    break
                except UnicodeDecodeError: continue
            
            knowledge_base += f"\n--- ФАЙЛ: {filename} ---\n{content}\n"
    return knowledge_base