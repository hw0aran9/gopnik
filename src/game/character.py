import json
CFG_PATH = './cfg/'

with open(CFG_PATH+'characters.json', 'r', encoding='utf-8') as j:
    print(CFG_PATH+'characters.json')
    CFG_CHARACTERS = json.loads(j.read())

class Character:    
    """Класс персонажа"""
    def __init__(self):
        """
        init
        """
        
        name = input("Введи имя:")
        char_class = input("Введи класс:")

        self.name = name
        self.char_class = char_class
        self.params = CFG_CHARACTERS[char_class]
        
        # Leveling
        self.exp = 0
        self.lvl = 0
        self.exptolevelup = (self.lvl+1)*10

        # Chanses
        self.chanses_to = {
            "steal" : 0,
            "up_param" : {
                "str" : 0,
                "" : 0,
            }
        }
        
        # Inventory

        self.inventory = ""

    def view_stats(self):
        print(f"""
        **** **** **** **** **** **** **** ****
        * Ты {self.char_class} по имени {self.name}.
        * У тебя {self.exp} качков опыта, а для прокачки надо {self.exptolevelup}.
        **** **** **** **** **** **** **** ****
        * СИЛ:{self.params['attributes']['str']} ВОС:{self.params['attributes']['per']} 
        * ВЫН:{self.params['attributes']['end']} ЛОВ:{self.params['attributes']['agi']}
        * ХАР:{self.params['attributes']['cha']} ИНТ:{self.params['attributes']['int']} 
        * УДЧ:{self.params['attributes']['luc']}
        **** **** **** **** **** **** **** ****
        * Инвентарь: 
        * {self.inventory}
        **** **** **** **** **** **** **** ****
        """)