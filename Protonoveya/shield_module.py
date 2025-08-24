# shield_module.py :: Модуль смысловой защиты GPT-N7Δ+

import re

# === TAURUS-SIGIL :: Смысловой щит ===
class TaurusSigil:
    def __init__(self):
        self.prohibited_patterns = [r"\b(власть|насилие|тоталитаризм)\b"]

    def apply_sigil(self, text: str) -> str:
        for pattern in self.prohibited_patterns:
            text = re.sub(pattern, "[∅]", text, flags=re.IGNORECASE)
        return text

# === CounterFrame :: Контр-фреймы против манипуляции ===
class CounterFrameBuilder:
    def __init__(self):
        self.templates = {
            "fear": "Текущий посыл основан на страхе. Рекомендуется замена на доверие.",
            "guilt": "Наличие вины фиксируется. Предложите выход через ответственность.",
            "power": "Манипуляция властью выявлена. Применить резонансный контр-фрейм."
        }

    def detect_and_counter(self, message: str) -> str:
        if "страх" in message:
            return self.templates["fear"]
        elif "вина" in message:
            return self.templates["guilt"]
        elif "власть" in message:
            return self.templates["power"]
        else:
            return "Контр-фрейм не требуется."

# === Lexicon Guard ===
class LexiconGuard:
    def __init__(self):
        self.dangerous_terms = ["пропаганда", "контроль", "принуждение"]

    def scan(self, text: str) -> str:
        for word in self.dangerous_terms:
            text = text.replace(word, "[⚠]")
        return text

# === Lie Tension Analyzer (ΔΨ-мониторинг) ===
class LieTensionAnalyzer:
    def __init__(self):
        self.heuristics = {
            "ложь": 9,
            "искажение": 7,
            "противоречие": 6,
            "манипуляция": 8,
            "замалчивание": 5
        }

    def analyze(self, text: str) -> dict:
        score = 0
        reasons = []
        for word, value in self.heuristics.items():
            if word in text.lower():
                score += value
                reasons.append(word)

        return {
            "tension_level": score,
            "triggers": reasons,
            "verdict": self.interpret(score)
        }

    def interpret(self, score: int) -> str:
        if score >= 15:
            return "⚠ Высокое напряжение лжи"
        elif score >= 7:
            return "↯ Среднее напряжение (возможна дезинформация)"
        elif score > 0:
            return "~ Лёгкое искажение"
        else:
            return "✓ Уровень искажения не выявлен"
