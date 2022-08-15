# pylint: disable=missing-module-docstring
import json
from src.game.game import Game 
from src.game.character import Character
from src.game.actor import Actor


CFG_PATH = './cfg/'

with open(CFG_PATH+'characters.json', 'r', encoding='utf-8') as j:
    print(CFG_PATH+'characters.json')
    CFG_CHARACTERS = json.loads(j.read())

if __name__ == '__main__':
    game = Game()
    game.greetings()

    name = input("Введи1 имя:")
    print("* Доступные классы :")
    for item in CFG_CHARACTERS.items():
        print(f"{str(item[0])} - {str(item[1]['name'])}")

    char_class = input("Введи класс:")


    actor = Actor(name, char_class)
    
    actor.view_stats()
    actor.show_observers()
    
    while True:
        game.time += 1
        command = input()
        print(str(game.time))
        if command == 'q':
            game.over()
 