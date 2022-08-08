# pylint: disable=missing-module-docstring
from src.game import game, character, location

game = game.Game()
actor = character.Character()
actor.view_stats()

while True:
    game.time += 1
    command = input()
    print(str(game.time))
    if command == 'q':
        game.over()
        