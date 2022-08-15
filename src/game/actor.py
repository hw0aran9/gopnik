"""
Модуль управления игроком
"""
CFG_PATH = './cfg/'

import json
from .character import Character

with open(CFG_PATH+'characters.json', 'r', encoding='utf-8') as j:
    print(CFG_PATH+'characters.json')
    CFG_CHARACTERS = json.loads(j.read())

class Actor(Character):
    """
    Player class
    """
    def __init__(self):
        """
        init
        """
        super().__init__()
    
        name = input("Введи имя:")
        print("* Доступные классы :")
        for item in CFG_CHARACTERS.items():
            print(f"{str(item[0])} - {str(item[1]['name'])}")

        char_class = input("Введи класс:")

        self.name = name
        self.char_class = char_class
        self.params = CFG_CHARACTERS[char_class]