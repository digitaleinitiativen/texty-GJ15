import re
from texty.graph import Action

class Parser:
    
    objects = [
        "katzenfutter", 
        "karton", 
        "raum",
        "staubsauger",
        "filet",
        "portal"
    ]
    
    actions = { 
    "fressen": 
        [
            "frisst", 
            "essen", 
            "friss", 
            "iss", 
            "fress", 
            "ess", 
            "fresse", 
            "esse"
        ],
    "schnurren":
        [
            "schnurrt",
            "schnurr",
            "schnurre",
        ],
    "aktivieren":
        [
            "aktiviere",
            "auslösen"
        ],
    "beamen":
        [
            "beame",
            "beam"
        ],
    "umsehen":
        [
            "herumsehen",
            "güggseln",
            "lugen"
        ],
    "schlafen":
        [
            "schlaf",
            "schlafe"
        ]
    }    
    
    
    def __init__(self, inputStr):
        self.inputStr = inputStr.lower()
    
    def match(self):
        action = self.match_action()
        obj = self.match_object()
        return Action(action, obj)
        
    def match_action(self):
        capwords = self.inputStr.split()
        for word in capwords:
            for action, action_deriv in Parser.actions.items():
                if word in action_deriv:
                    return action
                elif word == action:
                    return action
        return None

    def match_object(self):
        capwords = self.inputStr.split()
        for word in capwords:
            if word in Parser.objects:
                return word
        return None
