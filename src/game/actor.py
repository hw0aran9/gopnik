"""
Модуль управления игроком
"""
CFG_PATH = './cfg/'

import json
from .character import Character
from .game import Game

with open(CFG_PATH+'characters.json', 'r', encoding='utf-8') as j:
    print(CFG_PATH+'characters.json')
    CFG_CHARACTERS = json.loads(j.read())

class Actor(Character):
    """
    Player class
    """
    def __init__(self, name, char_class):
        """
        init
        """
        super().__init__(name, char_class)
        self.register(Game)

        self.name = name
        self.char_class = char_class
        self.params = CFG_CHARACTERS[char_class]

    def view_stats(self):
        """
        Отображение статистики персонажа
        """
        print(f"""
        ┌────────────────────────────────────────────────
        │ Ты {self.params['name']} по имени {self.name}.
        │ У тебя {self.exp} качков опыта, а для прокачки надо {self.exptolevelup}.
        ├────────────────────────────────────────────────
        │ СИЛ:{self.params['attributes']['str']} ВОС:{self.params['attributes']['per']} ВЫН:{self.params['attributes']['end']}
        │ ЛОВ:{self.params['attributes']['agi']} ХАР:{self.params['attributes']['cha']} ИНТ:{self.params['attributes']['int']} 
        │ УДЧ:{self.params['attributes']['luc']}
        ├────────────────────────────────────────────────
        │ Инвентарь: 
        │ {self.inventory}
        └────────────────────────────────────────────────
        """)

    def move_to(self):
        """
        Перемещение между игровыми локациями
        """
        pass

    def walk(self):
        Game().handle('actor_walked')