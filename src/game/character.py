import json
CFG_PATH = './cfg/'

with open(CFG_PATH+'characters.json', 'r', encoding='utf-8') as j:
    print(CFG_PATH+'characters.json')
    CFG_CHARACTERS = json.loads(j.read())

class Character:    
    """Класс персонажа"""
    def __init__(self,name,char_class):
        """
        init
        """
        self.name = name
        self.char_class = char_class
        self.params = CFG_CHARACTERS[char_class]
        print(f"Теперь ты {str(self.char_class)} по имени {str(self.name)}!")
        print(f"Params: {str(self.params)}")    

    def view_stats(self):
        STATS_TEMPLATE = f""