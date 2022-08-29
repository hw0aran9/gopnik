

class SceneHandler:
    def handle(self, scene, actor):
        raise NotImplementedError()

class OptionsHandler(SceneHandler):
    def handle(self, options_set):
        acceptable_ids = []
        for option in options_set:
            print(f"[{option.id}] {option.text}")
            acceptable_ids.append(option.id)
        
        while selected_id not in acceptable_ids:
            selected_id = input(selected_id)
        
class Option:
    def __init__(self, ):
        self.id = None

class TextHandler(SceneHandler):
    def handle(self, text):
        print(text)
        input()

