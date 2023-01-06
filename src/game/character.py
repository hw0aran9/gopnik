"""
Модуль управления персонажами
"""

import json
from .game import Observable
from .config import GAMEDATA_PATH

with open(GAMEDATA_PATH+'characters.json', 'r', encoding='utf-8') as j:
    CFG_CHARACTERS = json.loads(j.read())

class Character(Observable):
    """Класс персонажа"""
    def __init__(self, name, char_class):
        """
        init
        """
        super().__init__()

        # Name
        self.name = name
        self.char_class = char_class
        self.params = CFG_CHARACTERS[char_class]

        # Leveling
        self.exp = 0
        self.lvl = 0
        self.exptolevelup = (self.lvl+1)*10

        # Chanses
        # Inventory
        self.inventory = []


    def view_stats(self): # перенести в класс игры 
        """
        Отображение статистики персонажа
        """
        print(f"""
        **** **** **** **** **** **** **** ****
        * Это {self.params['name']} по имени {self.name}.
        **** **** **** **** **** **** **** ****
        * СИЛ:{self.params['attributes']['str']} ВОС:{self.params['attributes']['per']} 
        * ВЫН:{self.params['attributes']['end']} ЛОВ:{self.params['attributes']['agi']}
        * ХАР:{self.params['attributes']['cha']} ИНТ:{self.params['attributes']['int']} 
        * УДЧ:{self.params['attributes']['luc']}
        **** **** **** **** **** **** **** ****
        """)


    def kick(self, enemy) -> None:
        """
        Пинание
        """

    def steal():
        """
        Воровство денег
        """
    
    def show_observers(self):
        print(str(self.observers))
