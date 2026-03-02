import os, requests, json

ASANA_PAT = os.getenv("ASANA_PAT")
PROJECT_GID = os.getenv("ASANA_PROJECT_GID")

TASKS = [
    "[01-L] Governance: Хартия Суверенитета #Logos",
    "[02-L] Energy: Био-нормализация частот #Logos",
    "[03-L] Water: Философия Понтийского Моста #Logos",
    "[04-L] Food: Протокол генетической чистоты #Logos",
    "[05-L] Economy: Обоснование органического тарифа #Logos",
    "[06-L] Security: Манифест прозрачных сетей #Logos",
    "[07-L] Culture: Карта культурных кодов #Logos",
    "[08-L] Tech: Доктрина инженерного суверенитета #Logos",
    "[01-N] Governance: Протокол Субъект",
    "[02-N] Energy: Картирование Battery Buffer",
    "[03-N] Water: ТЗ очистки сероводорода",
    "[04-N] Food: Реестр локальных фермеров",
    "[05-N] Economy: Генератор юр. претензий",
    "[06-N] Security: CII-Audit Conflict Index",
    "[07-N] Culture: Протокол инфо-тишины",
    "[08-N] Tech: local_core.py настройка",
    "[01-T] Governance: Цифровой двойник Громады #Telos",
    "[02-T] Energy: Автономный узел Sigma #Telos",
    "[03-T] Water: Карта чистых источников #Telos",
    "[04-T] Food: Банк семян + маркет-плейс #Telos",
    "[05-T] Economy: Реестр аннулированных долгов #Telos",
    "[06-T] Security: Система Свой-Чужой #Telos",
    "[07-T] Culture: Издание Свода НОВЕЯ #Telos",
    "[08-T] Tech: Автономная инфраструктура Клешни #Telos"
]

def scale():
    if not ASANA_PAT or not PROJECT_GID:
        print("![Error] Переменные не установлены.")
        return
    
    headers = {"Authorization": f"Bearer {ASANA_PAT}"}
    print(f"Масштабирование проекта {PROJECT_GID} до 24 ветвей...")
    
    for t_name in TASKS:
        data = {"data": {"name": t_name, "projects": [PROJECT_GID]}}
        r = requests.post("https://app.asana.com/api/1.0/tasks", headers=headers, json=data)
        if r.status_code == 201:
            print(f"[+] Создано: {t_name}")
        else:
            print(f"[!] Ошибка: {t_name} - {r.text}")

if __name__ == "__main__":
    scale()
