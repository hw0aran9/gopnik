import json
from .actor import Actor

CFG_PATH = './cfg/'

with open(CFG_PATH+'commands.json', 'r', encoding='utf-8') as j:
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
        
