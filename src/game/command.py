from .actor import Actor

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
        
