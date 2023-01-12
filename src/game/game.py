"""
Класс управления игрой.
Отслеживает изменения  объектов игры, 
управляет правилами игры. 
"""

import json
from abc import ABCMeta, abstractmethod
import sys
import random
from art import tprint
from .config import GAMEDATA_PATH

with open(GAMEDATA_PATH+'events.json', 'r', encoding='utf-8') as j:
    CFG_EVENTS = json.loads(j.read())

with open(GAMEDATA_PATH+'cutscenes.json', 'r', encoding='utf-8') as j:
    CFG_CUTSCENES = json.loads(j.read())

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
        match message:
            case 'actor_walked':
                self.time +=1
                print(str(random.choice(CFG_EVENTS[message])))
            case 'actor_walked_to_market':
                self.time +=1
                print('Ты пришел на рынок')
            case 'char_kicked':
                print('Игра: Подтверждаю - пинок был осуществлен.,l')

        print(f"{self.name} notified that {message}")

    def greet(self):
        tprint("Klon Gopnika")

    def save(self):
        """
        save game
        """

    def load(self):
        """
        load
        """

    def over(self):
        tprint('GAME OVER')
        sys.exit(0)
        