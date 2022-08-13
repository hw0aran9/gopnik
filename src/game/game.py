"""
Класс управления игрой.
Отслеживает изменения  объектов игры, 
управляет правилами игры. 
"""
from abc import ABCMeta, abstractmethod
import sys
import random

class Observer(metaclass=ABCMeta):
    """
    Абстрактный класс-наблюдатель
    """
    @abstractmethod
    def update(self, message:str) -> None: 
        """
        Получение нового сообщения
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
        Регистрация нового наблюдателя за классом
        """
        self.observers.append(observer)
        print(f"registered {str(observer)} as observer.")

    def notify_observers(self, message:str) -> None:
        """
        Уведомление всем наблюдателям, 
        которые подписаны на события объекта
        наблюдаемого класса
        """
        for obs in self.observers:
            obs.update(message)

class Game(Observer):
    """
    Game class
    """
    def __init__(self):
        self.time = 0
        random.seed()

    def update(self, message:str) -> None:
        print(f"{self.name} notified about: {message}")

    def greetings(self):
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
        sys.exit()

    