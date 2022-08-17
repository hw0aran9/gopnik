# pylint: disable=missing-module-docstring
import json
from src.game.game import Game 
from src.game.actor import Actor
from src.game.command import Command

CFG_PATH = './cfg/'
global g_some_var
with open(CFG_PATH+'characters.json', 'r', encoding='utf-8') as j:
    CFG_CHARACTERS = json.loads(j.read())

def main():
    game = Game()
    game.greet()
    game.play("intro2")

    name = input("Введи имя:")
    print("* Доступные классы :")
    for item in CFG_CHARACTERS.items():
        print(f"{str(item[0])} - {str(item[1]['name'])}")

    char_class = input("Введи класс:")
    actor = Actor(name, char_class)
    actor.view_stats()
    
    while True:
        game.time += 1
        command = input()
        if command == 'q':
            game.over()
        elif command == 'w':
            actor.walk()
        elif command == 'time': 
            print(game.time)

if __name__ == '__main__':
    main()

