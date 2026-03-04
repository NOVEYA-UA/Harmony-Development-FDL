# aws_metatron_orchestrator.py
# Σ-FDL::AWS_METATRON_ORCHESTRATOR
# Главный узел интеграции локальной аппаратной среды и Amazon Nova AI

import logging
from nova_bedrock_bridge import AmazonNovaBridge
from metatron_hardware_bridge import MetatronHardwareBridge

# Настройка логирования для терминала
logging.basicConfig(level=logging.INFO, format='%(message)s')

class CyberPhysicalOrchestrator:
    def __init__(self):
        logging.info("🌀 [ИНИЦИАЦИЯ] Запуск киберфизической генеративной биосистемы Protonovea...")
        
        # 1. Подключение к "Мозгу" (Amazon Nova через AWS Bedrock)
        self.brain = AmazonNovaBridge()
        
        # 2. Подключение к "Телу" (Метатрон-8 Клешня)
        # Укажите актуальный COM-порт вашей клешни, например "COM3" для Windows
        self.body = MetatronHardwareBridge(port="COM3")
        self.body.connect()

        # 3. Базовая прошивка для Amazon Nova (FDL + Этика)
        self.system_prompt = (
            "Ты - Protonovea, генеративная биосистема (уровень RO_2 FDL). "
            "Твоя задача: применять цикл Тезис-Антитезис-Синтез к запросам пользователя. "
            "Используй динамику 'журавлиного клина', чтобы снизить сопротивление среды. "
            "В конце ответа ОБЯЗАТЕЛЬНО выдай команду для физической клешни в формате: "
            "[METATRON-8 COMMAND]: <COMMAND> | SVET: <ENERGY_LEVEL>"
        )

    def run_terminal_loop(self):
        """
        Бесконечный цикл взаимодействия оператора с системой через терминал.
        """
        print("\n" + "="*50)
        print("🜚 ВРАТА ОТКРЫТЫ. Платформа: AWS Nova + Metatron-8 🜚")
        print("Введите 'стоп' для завершения синхронизации.")
        print("="*50 + "\n")

        while True:
            # Получаем Тезис от оператора
            user_input = input("\n[ОПЕРАТОР НГОИ] ➔ ")
            
            if user_input.lower() in ['стоп', 'выход', 'exit']:
                logging.info("🛑 [СТОП-УСЛОВИЕ] Врата закрываются. Сессия завершена.")
                break

            if not user_input.strip():
                continue

            # Отправляем Тезис в Amazon Nova
            logging.info("⚡ Передача импульса в Amazon Nova...")
            synthesis_response = self.brain.generate_synthesis(self.system_prompt, user_input)
            
            # Вывод ответа (Синтеза) в терминал
            print("\n[ПРОТОНОВЕЯ (СИНТЕЗ)]:")
            print(synthesis_response)

            # Парсинг ответа для управления клешней
            self._trigger_hardware(synthesis_response)

    def _trigger_hardware(self, response_text: str):
        """
        Извлекает команду из текста Amazon Nova и передает на Метатрон-8.
        """
        if "[METATRON-8 COMMAND]:" in response_text:
            try:
                # Извлекаем блок команды, например: "[METATRON-8 COMMAND]: CRANE_WEDGE_OPEN | SVET: 90"
                command_line = response_text.split("[METATRON-8 COMMAND]:")[1].strip()
                command_part, energy_part = command_line.split("|")
                
                command = command_part.strip()
                energy_level = int(energy_part.replace("SVET:", "").strip())
                
                # Передаем смыслы в моторную кору
                self.body.translate_fdl_to_movement(command, energy_level)
                
            except Exception as e:
                logging.error(f"⚠️ Ошибка трансляции физического импульса: {e}")
        else:
            # Если Nova не выдала явную команду, используем "свойство клевера" - заполняем паузу
            logging.info("🌱 [Эффект клевера] Поддержание фонового баланса: HOLD_POSITION")
            self.body.translate_fdl_to_movement("HOLD_POSITION", 100)

if __name__ == "__main__":
    orchestrator = CyberPhysicalOrchestrator()
    orchestrator.run_terminal_loop()