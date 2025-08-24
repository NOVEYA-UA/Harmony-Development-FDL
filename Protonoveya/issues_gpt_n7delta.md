# 📋 GPT-N7Δ+ :: Issue Tracker

## [#1] CONFIG_PATH несоответствие
- 📂 Модуль: `resonance_module.py`
- 🔥 Проблема: Ожидает `resonance_nucleus.json` в `config/`, но файл находится в корне.
- ✅ Решение: Изменить путь на `Path("resonance_nucleus.json")`

## [#2] Нет защиты при JSON-загрузке
- 📂 Модуль: `resonance_module.py`
- 🛡 Предлагается: обернуть `json.load(f)` в try–except

## [#3] Отсутствие юнит-тестов
- 📦 Общая сборка
- 💡 Рекомендуется: создать папку `tests/` с `pytest`

## [#4] Расширить FDLGraphEngine
- 📂 Модуль: `visualization_module.py`
- 💡 Добавить layout: `shell`, `kamada_kawai`, `planar`

## [#5] Централизация ошибок в логике
- 📂 Модуль: `blessing_cycle`, `main.py`
- 💡 Выделить `ErrorHandler` или хотя бы `logger.error(...)`

## [#6] Докеризация без ENV-защиты
- 📂 `Dockerfile.txt`
- ⚠ `shared_secret`, пути — жёстко зашиты. Перенести в `.env`
