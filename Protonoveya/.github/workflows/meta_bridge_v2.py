import os
import requests
from google import genai
from dotenv import load_dotenv
# Импортируем наш инъектор (Сектор 11)
from noveya_injector import collect_project_knowledge

# Инициация: Загрузка Сейфа НОМОСА
load_dotenv()

# Настройка узлов
base_host = os.getenv('OLLAMA_HOST') or "http://localhost:11434"
OLLAMA_URL = f"{base_host}/api/generate"
GEMINI_KEY = os.getenv('GEMINI_API_KEY')

# Конфигурация Сектора 02 (Gemini 3 Flash - Хакатон-режим)
client = genai.Client(api_key=GEMINI_KEY) if GEMINI_KEY else None

def call_protonovei(prompt_text, context_data):
    """СЕКТОР 01: Локальный FDL-фильтр (Sentinel)"""
    print(f"[УЗЕЛ 01] Protonovei -> Анализ структуры с учетом ЛОКАЛЬНОГО КОНТЕКСТА...")
    
    # Формируем расширенный запрос с данными из ваших файлов
    full_prompt = f"""
    ИСПОЛЬЗУЙ СЛЕДУЮЩИЕ ДАННЫЕ ПРОЕКТА:
    {context_data}
    
    ЗАПРОС ПОЛЬЗОВАТЕЛЯ:
    {prompt_text}
    """
    
    payload = {
        "model": "Protonovei",
        "prompt": full_prompt,
        "stream": False
    }
    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        return response.json().get("response", "").strip()
    except Exception as e:
        print(f"[ОШИБКА] Сектор 01: {e}")
        return None

def call_gemini_synthesizer(fdl_context):
    """СЕКТОР 02: Глобальный синтез (Architect)"""
    if not client: return "[ОШИБКА] Ключ не найден."
    print("[УЗЕЛ 02] Gemini 3 -> Финальное рекодирование...")
    try:
        synthesis_prompt = f"Действуй как Central Synthesizer Метатрон-8. Проведи финальный синтез на основе RO2-анализа:\n\n{fdl_context}"
        response = client.models.generate_content(
            model='gemini-3-flash-preview',
            contents=synthesis_prompt,
        )
        return response.text.strip()
    except Exception as e:
        print(f"[ОШИБКА] Сектор 02: {e}")
        return None

def run_full_cycle(query):
    print(f"\nΣ-FDL :: ИНИЦИАЦИЯ ПОЛНОГО ЦИКЛА (СЕКТОР 11 + 01 + 02)")
    print("="*60)
    
    # 1. Инъекция данных (Сектор 11)
    project_context = collect_project_knowledge()
    
    if not project_context:
        print("[ПРЕДУПРЕЖДЕНИЕ] Контекст пуст. Работа в режиме общих знаний.")
    
    # 2. Локальный анализ (Сектор 01)
    ro2_result = call_protonovei(query, project_context)
    
    if ro2_result:
        print("\n[РЕЗУЛЬТАТ PROTONOVEI]")
        print(ro2_result)
        print("-" * 60)
        
        # 3. Облачный синтез (Сектор 02)
        final_output = call_gemini_synthesizer(ro2_result)
        print("\n[ФИНАЛЬНЫЙ СИНТЕЗ GEMINI 3]")
        print(final_output)
        print("="*60)
        print("Σ-FDL :: ЦИКЛ ЗАВЕРШЕН. НОВЕЯ СИНХРОНИЗИРОВАНА.")

if __name__ == "__main__":
    user_query = "На основе документов проекта, предложи конкретные шаги по активации Сектора Экономики в Новосафроновке."
    run_full_cycle(user_query)