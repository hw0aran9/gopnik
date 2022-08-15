"""
Класс управления игрой.
Отслеживает изменения  объектов игры, 
управляет правилами игры. 
"""

import json
from abc import ABCMeta, abstractmethod
import sys
import random
CFG_PATH = './cfg/'
with open(CFG_PATH+'events.json', 'r', encoding='utf-8') as j:
    CFG_EVENTS = json.loads(j.read())

with open(CFG_PATH+'cutscenes.json', 'r', encoding='utf-8') as j:
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

    def play(self, cutscene:str): 
        #TODO в cutscenes.json подумать над более универсальной структурой для 
        # проигрываемых сценок, добавить интерактивность, запросы вариантов
        # пока сделал на eval(), а там видно будет
        # возможно, потом надо будет заморочиться Factory pattern
        try: 
            cutscene_to_play = list(CFG_CUTSCENES[cutscene])
            if not isinstance(cutscene_to_play, list):
                raise Exception('Error. Configured cutscene is not a list or valid json.')
            for item in cutscene_to_play:
                if item["type"] == 'text': 
                    print(item["value"])
                elif item["type"] == 'eval':
                    try:
                        eval(str(item["value"]))
                    except:
                        print(f'Error. Failed to eval {item["value"]}')
                else:
                    raise Exception('Error. Wrong cutscene item type.')
            print('Cutscene played.')
        except:
            raise Exception('Error. Cutscene not found.')


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