# pylint: disable=missing-module-docstring

from src.game.game import Game 
from src.game.character import Character



if __name__ == '__main__':
    game = Game()
    game.greetings()
    actor = Character()
    actor.register(Game)
    actor.view_stats()
    
    while True:
        game.time += 1
        command = input()
        print(str(game.time))
        if command == 'q':
            game.over()
 