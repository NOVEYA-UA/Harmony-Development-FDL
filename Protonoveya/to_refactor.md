# 🧬 GPT-N7Δ+ :: Refactor Points

## I. Логическая сборка
- [ ] Разбить `process_stage()` на отдельные классы: `StageCollector`, `StageAnalyzer`, etc.
- [ ] Вынести формулу Tr в отдельный модуль (e.g. `norm_calculator.py`)

## II. Безопасность
- [ ] Добавить fallback-конфигурацию, если JSON не загружен
- [ ] Обернуть `hash(str(input_data))` в try–except

## III. Интерфейс и визуализация
- [ ] Добавить в `FDLGraphEngine`:
  - выбор layout
  - сохранение в PNG/SVG
  - экспорт JSON-структур

## IV. CLI / API
- [ ] `run_demo_cycle()` → в `demo_runner.py`
- [ ] API → добавить `/fdl/export` endpoint

## V. Устойчивость
- [ ] Проверка всех путей через `Path().resolve().exists()`
- [ ] Модули фильтрации подключать через DI-контейнер (например, simple registry)
