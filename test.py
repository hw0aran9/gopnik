import json
from src.game.game import Game 
from src.game.actor import Actor
from src.game.command import Command
from src.game.cutscene import *

CFG_PATH = './cfg/'
global g_some_var
with open(CFG_PATH+'characters.json', 'r', encoding='utf-8') as j:
    CFG_CHARACTERS = json.loads(j.read())

with open(CFG_PATH+'cutscenes.json', 'r', encoding='utf-8') as j:
    CFG_CUTSCENES = json.loads(j.read())

oh = OptionsHandler()
