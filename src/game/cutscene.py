class SceneHandler:
    def handle(self, scene, actor):
        raise NotImplementedError()

class Option:
    def __init__(self, id, text, consequences):
        self.id = id
        self.text = text
        self.consequences = consequences #тут дописать надо, как из файла вычитать данные для инициализации консиквенса
    
    def select(self, id):
        for consequence in self.consequences:
            conseq = Consequenсe(consequence["object"], consequence["attr"], consequence["value"])
            conseq.affect()

class Consequenсe:
    def __init__(self, affected_object, attribute, value):
        self.affected_object = eval(affected_object)
        self.attribute = attribute
        self.value = eval(value)
    
    def affect(self):
        try:
            setattr(self.affected_object, self.attribute, self.value)
        except:
            print(f"Failed to set attribute {str(self.attribute)} to {self.value} on {str(self.affected_object)}")

class OptionsHandler(SceneHandler):
    def handle(self, options_set):
        acceptable_ids = []
        for option in options_set:
            print(f"[{option.id}] {option.text}")
            acceptable_ids.append(option.id)
        
        while selected_id not in acceptable_ids:
            selected_id = input(selected_id)

class TextHandler(SceneHandler):
    def handle(self, text_list):
        for text in text_list:
            input(text)

