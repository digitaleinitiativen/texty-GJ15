
from texty.graph import Action

class Parser:

    actions = {
        "hilfe": [],
        "holen": [
            'hola'
        ],
        "spielen": [
            "spiela"
        ],
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
                "schnurra",
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
                "schau herum",
                "umma schaua",
                "umhersehen",
                "güggseln",
                "lugen",
                "aschaua",
                "anschauen",
                "ansehen"
            ],
        "schlafen":
            [
                "schlaf",
                "schlofa",
                "schlafe"
            ]
    }

    def __init__(self, inputStr, objects):
        self.inputStr = inputStr.lower()
        self.objects = objects

    def match(self):
        words = self.inputStr.split()
        action = self._match(words, Parser.actions)
        obj = self._match(words, self.objects)
        return Action(action, obj)

    def _match(self, words, possibilities):
        for word in words:
            for name, synonyms in possibilities.items():
                if word in synonyms:
                    return name
                elif word == name:
                    return name
                if name in self.inputStr:
                    return name
                for synonym in synonyms:
                    if synonym in self.inputStr:
                        return name
        return None

    def match_object(self):
        capwords = self.inputStr.split()
        for word in capwords:
            if word in Parser.objects:
                return word
        return None
