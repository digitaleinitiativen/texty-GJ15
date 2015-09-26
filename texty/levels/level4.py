
from texty.graph import Node

class Level(Node):
    def __init__(self):
        description = 'TODO'
        super().__init__(description, actions={}, objects={})


level4 = Level()
