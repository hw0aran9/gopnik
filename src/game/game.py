"""
Класс управления игрой.
Отслеживает изменения  объектов игры, 
управляет правилами игры. 
"""
CFG_PATH = './cfg/'
import json
from abc import ABCMeta, abstractmethod
import sys
import random

class Observer(metaclass=ABCMeta):
    """
    Абстрактный класс-наблюдатель
    """
    @abstractmethod
    def handle(self, message:str) -> None: 
        """
        Обработка нового сообщения
        """
        pass

class Observable(metaclass=ABCMeta):
    """
    Абстрактный класс наблюдаемого объекта
    """

    def __init__(self) -> None: 
        """
        Конструктор
        """
        self.observers = [] #список наблюдателей

    def register(self, observer: Observer) -> None:
        """
        Подписать на экземпляр класса нового наблюдателя
        """
        self.observers.append(observer)
        print(f"registered {str(observer.__repr__)} as observer.")
    def notify_observers(self, message:str) -> None:
        """
        Уведомление всем наблюдателям, 
        которые подписаны на события объекта
        наблюдаемого класса
        """
        for obs in self.observers:
            obs.handle(message)

class Game(Observer):
    """
    Основной класс игры. 
    Управляет, отслеживает, 
    списывает, начисляет. 
    """
    def __init__(self):
        self.time = 0
        self.name = 'Dungeon master'
        random.seed()

    def handle(self, message:str) -> None:
        with open(CFG_PATH+'events.json', 'r', encoding='utf-8') as j:
            CFG_EVENTS = json.loads(j.read())
        
        match message:
            case 'actor_walked':
                print(str(random.choice(CFG_EVENTS[message])))
        
        print(f"{self.name} notified about: {message}")

    def greet(self):
        LINES = [
      "┌─── ┌───┐ ┌───┐ ╷   ╷ ╷   ╷ ╷   ╷",
      "│    │   │ │   │ │   │ │   │ │  ╱ ",
      "│    │   │ │   │ │   │ │   │ │ ╱  ",
      "│    │   │ │   │ ├───┤ │  ╱│ │╱   ",
      "│    │   │ │   │ │   │ │ ╱ │ │╲   ",
      "│    │   │ │   │ │   │ │╱  │ │ ╲  ",
      "│    │   │ │   │ │   │ │   │ │  ╲ ",
      "╵    └───┘ ╵   ╵ ╵   ╵ ╵   ╵ ╵   ╵",
      "          Беспредел в Ульяновске  ",
    ]

    def play(self, cutscene): 
        #TODO в cutscenes.json подумать над более универсальной структурой для проигрываемых сценок, добавить интерактивность, запросы вариантов
        pass

    def save(self):
        """
        save game
        """

    def load(self):
        """
        load
        """

    def over(self):
        print('Game over!')
        sys.exit(0)