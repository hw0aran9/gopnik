# pylint: disable=missing-module-docstring

from src.game import character

 

name = input("Введи имя:")
char_class = input("Введи класс:")

actor = character.Character(name, char_class)