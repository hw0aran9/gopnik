"""
Модуль управления игроком
"""
CFG_PATH = './cfg/'

import json
from transitions import Machine
from .character import Character
from .game import Game

with open(CFG_PATH+'characters.json', 'r', encoding='utf-8') as j:
    CFG_CHARACTERS = json.loads(j.read())

with open(CFG_PATH+'locations.json', 'r', encoding='utf-8') as j:
    CFG_LOCATIONS = json.loads(j.read())

with open(CFG_PATH+'transitions.json', 'r', encoding='utf-8') as j:
    CFG_TRANSITIONS = json.loads(j.read())

class Actor(Character):
    """
    Player class
    """
    states = list(CFG_LOCATIONS.keys())
    transitions = list(CFG_TRANSITIONS)
    def __init__(self, name, char_class):
        """
        init
        """
        super().__init__(name, char_class)
        self.register(Game)

        self.name = name
        self.char_class = char_class
        self.params = CFG_CHARACTERS[char_class]
        
        # Конечный автомат, описывающий допустимые 
        # переходы между игровыми уровнями
        self.machine = Machine(model=self, states=Actor.states, transitions=Actor.transitions, initial='l00_idle')

    def view_stats(self):
        """
        Отображение статистики персонажа
        """
        print(f"""
        Ты находишься на локации: {self.state}
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

    def move_to(self, destination):
        """
        Перемещение между игровыми локациями
        """
        match destination:
            case 'l02_market': 
                self.to_market()
                Game().handle('actor_walked_to_market')

    def walk(self):
        self.to_idle()
        Game().handle('actor_walked')