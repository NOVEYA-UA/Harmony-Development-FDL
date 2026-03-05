import os

def collect_project_knowledge(directory=r"C:\СОЦИАЛЬНЫЙ ПРОЕКТ НОВЕЯ"):
    knowledge_base = ""
    print(f"Σ-FDL :: СЕКТОР 11 :: Сканирование папки {directory}...")
    
    if not os.path.exists(directory):
        print(f"[ОШИБКА] Директория не найдена: {directory}")
        return ""

    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            print(f" -> Поглощение данных: {filename}")
            filepath = os.path.join(directory, filename)
            
            # Снятие дискретности кодировок: пробуем UTF-8, при неудаче — Windows-1251
            content = ""
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
            except UnicodeDecodeError:
                try:
                    with open(filepath, 'r', encoding='windows-1251') as f:
                        content = f.read()
                except Exception as e:
                    print(f"[ШУМ] Не удалось прочитать {filename}: {e}")
                    continue
            
            knowledge_base += f"\n--- ФАЙЛ: {filename} ---\n{content}\n"
    
    return knowledge_base
