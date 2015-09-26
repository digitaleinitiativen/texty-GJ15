
from texty.graph import Action

class Parser:

    objects = {
        "katzenfutter": [],
        "karton": [],
        "raum": [],
        "staubsauger": [],
        "filet": [],
        "portal": [
            'katzenklappe'
        ]
    }

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
            "beam",
            "betreten",
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
        words = self.inputStr.split()
        action = self._match(words, Parser.actions)
        obj = self._match(words, Parser.objects)
        return Action(action, obj)

    def _match(self, words, possibilities):
        for word in words:
            for name, synonyms in possibilities.items():
                if word in synonyms:
                    return name
                elif word == name:
                    return name
        return None

    def match_object(self):
        capwords = self.inputStr.split()
        for word in capwords:
            if word in Parser.objects:
                return word
        return None
