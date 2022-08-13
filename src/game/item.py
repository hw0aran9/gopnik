"""
Модуль управления игровым шмотом. 
"""
from .game import Observable, Observer

class Item(Observable, Observer):
    """
    Класс внутриигрового предмета
    """
    def __init__(self):
        self.price = 0
        self.name = ""
        self.slot = ""
        