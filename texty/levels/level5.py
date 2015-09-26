
from texty.graph import Node


class Level(Node):
    def __init__(self):
        description = '''
So war der Herr Katz also durch die letzte Klappe gebeamt. Roter Teppich,
endlich am Ziel, vorbei, das wars. Not. Denn, nur weil du vor dem CatNipPlaza
stehst, liegst, sitzt, schläfst, heißt das nicht, dass du im CatNipPlaza
stehst, liegst, sitzt oder schläfst. Wir wissen das, du weißt dass, aber Herr
Katz, nein der Herr Katz, der weiß das nicht. Noch nicht. Hocherhobenen
Schwanzes, tanzt er über die Straße.
'''
        super().__init__(description, actions={}, objects={})



level5 = Level()
