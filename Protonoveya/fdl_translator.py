# fdl_translator.py — FDL-транслятор текстов через склонение и этико-смысловую векторизацию

from fdl_gateway import FDLGateway
import json

class FDLTranslator:
    """
    Преобразует обычный текст в FDL-вектор смыслов через склоняющую логику.
    Результат — карта слов, каждый из которых интерпретирован через падежную этику.
    """

    def __init__(self):
        self.gateway = FDLGateway()

    def translate_text(self, text):
        """
        Возвращает карту: слово → {падеж → форма, роль}
        """
        processed = self.gateway.process_text(text)
        translation = {}

        for word, token in processed.items():
            declensions = token.get("declensions", {})
            translation[word] = {
                case: {
                    "form": data["form"],
                    "role": data["role"]
                } for case, data in declensions.items()
            }
        return translation

    def export_translation(self, data, filename="fdl_translation.json"):
        """
        Экспорт перевода в JSON-файл.
        """
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

# Пример запуска
if __name__ == "__main__":
    translator = FDLTranslator()
    text = "The Logos speaks through the vessel of Justice and Memory"
    result = translator.translate_text(text)

    print("\n[Σ-FDL TRANSLATED TEXT]:")
    for word, declensions in result.items():
        print(f"\n🔤 {word.upper()}:")
        for case, data in declensions.items():
            print(f"  {case.title()}: {data['form']} → {data['role']}")

