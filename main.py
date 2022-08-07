# pylint: disable=missing-module-docstring

from src.game import character
from src.game import location

actor = character.Character()
actor.view_stats()

while True:
    command = input()
    if command == 'q': 
        break