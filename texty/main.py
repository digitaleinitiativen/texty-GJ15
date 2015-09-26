
import os
from texty.levels import level1
from texty.parser import Parser
from .screen import MainScreen


here = os.path.abspath(os.path.dirname(__file__))
images = os.path.join(here, 'images')

import pyglet.resource
pyglet.resource.path = [images]
pyglet.resource.reindex()


class Main():

    def __init__(self):
        self.node = level1
        self.screen = MainScreen(self.got_text)
        if self.node.background:
            self.screen.background.image = self.node.background
        self.screen.text(self.node.description)
        self.screen.run()

    def got_text(self, text):
        p = Parser(text)
        self.node = self.node.do(p.match())
        self.screen.text(self.node.description)
        if self.node.background:
            self.screen.background.image = self.node.background


def main():
    Main()


if __name__ == '__main__':
    main()
