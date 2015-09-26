import re
from texty.graph import Action

class Parser:
    
    objects = ["Katzenfutter", "Karton", "Raum"]
    actions = ["fressen", "trinken", "gehen", "schnurren", "miauen"]
    
    def __init__(self, inputStr):
        self.inputStr = inputStr
    
    def match(self):
        action = self.match_action()
        obj = self.match_object()
        return Action(action, obj)
        
    def match_action(self):
        capwords = self.inputStr.split()
        for word in capwords:
            if word in Parser.actions:
                return word
        return None

    def match_object(self):
        capwords = self.inputStr.split()
        for word in capwords:
            if word in Parser.objects:
                return word
        return None
