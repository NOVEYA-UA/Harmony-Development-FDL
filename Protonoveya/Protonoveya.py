import time
import random

# Базовый класс элемента системы
class Element:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = []  # Связи между элементами

    def connect(self, other_element):
        """Создание связей между элементами"""
        if other_element not in self.connections:
            self.connections.append(other_element)
            other_element.connect(self)  # Двусторонняя связь

    def process(self, input_data):
        """Обработка данных в элементе"""
        raise NotImplementedError("Метод process() должен быть реализован в каждом элементе")

# Четыре основных элемента
class Earth(Element):
    def process(self, input_data):
        time.sleep(0.5)
        return f"🌍 Земля (структура): организует данные -> {input_data}"

class Water(Element):
    def process(self, input_data):
        time.sleep(0.5)
        return f"💧 Вода (гибкость): адаптирует информацию -> {input_data}"

class Fire(Element):
    def process(self, input_data):
        time.sleep(0.5)
        return f"🔥 Огонь (генерация): создаёт новую идею -> {input_data}"

class Air(Element):
    def process(self, input_data):
        time.sleep(0.5)
        return f"🌬️ Воздух (коммуникация): передаёт знания -> {input_data}"

# Центральный элемент - Протоновея
class Pranovea(Element):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.energy_level = 100
        self.harmony = True
        self.social_balance = 100
        self.ethical_justice = 100
        self.resource_distribution = 100

    def process(self, input_data):
        time.sleep(0.5)
        return f"⚛️ Протоновея (система): объединяет элементы -> {input_data}"

    def balance_energy(self, input_energy):
        if input_energy > 120:
            self.harmony = False
            return "Перегрузка! Система стабилизируется..."
        elif input_energy < 80:
            self.harmony = False
            return "Энергии недостаточно. Активация резонанса..."
        else:
            self.harmony = True
            return "Баланс энергии сохранён."

# Центральное ядро - Оболочка СВЕТ
class Core:
    def __init__(self):
        self.elements = []

    def add_element(self, element):
        self.elements.append(element)

    def synchronize(self):
        """Синхронизация всех элементов"""
        print("\n⚡ Оболочка СВЕТ активирована ⚡\n")
        for element in self.elements:
            print(f"🔗 {element.name} подключен к системе.")
        
        time.sleep(1)
        
        for element in self.elements:
            print(f"\n🔄 Взаимодействие {element.name}:")
            for connection in element.connections:
                processed_data = connection.process(f"данные от {element.name}")
                print(processed_data)

        print("\n✅ Все элементы синхронизированы! Протоновея активна.")

    def activate(self):
        """Активация ядра, связывающего все элементы"""
        print("🚀 Запуск системы...\n")
        self.synchronize()

# Создаём элементы
earth = Earth("Земля", "Структурирование информации")
water = Water("Вода", "Гибкость и адаптация")
fire = Fire("Огонь", "Генерация новых идей")
air = Air("Воздух", "Коммуникация и взаимодействие")
pranovea = Pranovea("Протоновея", "Связующее звено, балансирующее систему")

# Добавляем элементы в ядро
core = Core()
core.add_element(earth)
core.add_element(water)
core.add_element(fire)
core.add_element(air)
core.add_element(pranovea)

# Устанавливаем связи между элементами
earth.connect(water)
water.connect(fire)
fire.connect(air)
air.connect(earth)
pranovea.connect(earth)
pranovea.connect(water)
pranovea.connect(fire)
pranovea.connect(air)

# Запускаем систему
core.activate()
