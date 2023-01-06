
# pylint: disable=missing-module-docstring
import json
from src.game.game import Game 
from src.game.actor import Actor
from src.game.command import Command
from src.game.cutscene import *

CFG_PATH = './cfg/'
global g_some_var
with open(CFG_PATH+'characters.json', 'r', encoding='utf-8') as j:
    CFG_CHARACTERS = json.loads(j.read())

with open(CFG_PATH+'cutscenes.json', 'r', encoding='utf-8') as j:
    CFG_CUTSCENES = json.loads(j.read())

def main():
    game = Game()
    game.greet()
    
    th = TextHandler()
    th.handle(CFG_CUTSCENES['intro'])

    name = input("Введи имя:")
    print("* Доступные классы :")
    for item in CFG_CHARACTERS.items():
        print(f"{str(item[0])} - {str(item[1]['name'])}")

    char_class = input("Введи класс:")
    actor = Actor(name, char_class)
    actor.view_stats()
    
    print(game.__dict__)

    while True:
        game.time += 1
        command = input()
        if command == 'q':
            game.over()
        elif command == 'w':
            actor.walk()
        elif command == 'time': 
            print(str(game.time))
        elif command == 'mar':
            actor.move_to('l02_market')
        elif command == 'i':
            actor.view_stats()

if __name__ == '__main__':
    main()

