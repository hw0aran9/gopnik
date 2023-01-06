import json
from .actor import Actor
from .config import GAMEDATA_PATH

with open(GAMEDATA_PATH+'commands.json', 'r', encoding='utf-8') as j:
    CFG_COMMANDS = json.loads(j.read())


class Command(): 
    """
    Команды игрового движка
    """
    def __init__(self):
        """
        init
        """
        pass
    
    def handle(self, command):
        command_list = ['w', '']
        
