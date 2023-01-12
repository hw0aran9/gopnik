
# pylint: disable=missing-module-docstring
# TODO подумать про curses
# TODO что-то с цветным шрифтом

import json
from pick import pick
from src.game.game import Game 
from src.game.actor import Actor
from src.game.cutscene import *
from src.game.config import GAMEDATA_PATH

with open(GAMEDATA_PATH+'characters.json', 'r', encoding='utf-8') as j:
    CFG_CHARACTERS = json.loads(j.read())

with open(GAMEDATA_PATH+'cutscenes.json', 'r', encoding='utf-8') as j:
    CFG_CUTSCENES = json.loads(j.read())

def main():
    game = Game()
    game.greet()

    th = TextHandler()
    #th.handle(CFG_CUTSCENES['intro'])

    name = input("Введи имя:")
    # print("* Доступные классы :")
    # for item in CFG_CHARACTERS.items():
    #    print(f"{str(item[0])} - {str(item[1]['name'])}")

    # char_class = input("Введи класс:")

    title = 'Выбери класс:'
    options = [(item[0],item[1]['name']) for item in CFG_CHARACTERS.items()]

    selected_class = pick(options, title)[0][0]
    
    actor = Actor(name, selected_class)
    actor.view_stats()
    
    while True:
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
        elif command == 'k':
            actor.kick(actor)

if __name__ == '__main__':
    main()
