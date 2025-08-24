class PadezhSklonLogic:
    """
    FDL-модуль склонения смысла: восстановление падежной этики через грамматические формы.
    Склонение как способ этической ориентации в языковом поле.
    """

    def __init__(self, word):
        self.word = word
        self.forms = self.decline()

    def decline(self):
        """
        Возвращает все падежные формы слова с их смысловыми ролями в Логос-структуре.
        """
        return {
            "nominative": {
                "form": self.word,
                "role": "Субъект. Изначальное имя. Точка Логоса."
            },
            "genitive": {
                "form": f"of {self.word}",
                "role": "Источник. Род. Связь с Истоком."
            },
            "dative": {
                "form": f"to {self.word}",
                "role": "Получатель. Дар. Направление воли."
            },
            "accusative": {
                "form": f"{self.word} (targeted)",
                "role": "Объект. Пациенс. Испытание действия."
            },
            "instrumental": {
                "form": f"with {self.word}",
                "role": "Орудие. Ангел. Энергия."
            },
            "locative": {
                "form": f"in {self.word}",
                "role": "Место. Пространство смысла."
            },
            "ablative": {
                "form": f"from {self.word}",
                "role": "Исход. Отступление. Освобождение."
            },
            "vocative": {
                "form": f"O {self.word}!",
                "role": "Призыв. Отклик. Молитва."
            }
        }

    def display(self):
        print(f"\nFDL-Склонение слова: {self.word}\n")
        for case, data in self.forms.items():
            print(f"{case.title()}: {data['form']} — {data['role']}")

# Пример использования
if __name__ == "__main__":
    example = PadezhSklonLogic("Logos")
    example.display()

