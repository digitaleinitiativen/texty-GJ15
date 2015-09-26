
import os
import cocos
from texty.levels import level1
from texty.parser import Parser
from texty.graph import Node, Game
from .screen import MainScreen
from cocos.scene import Scene



class Main():

    def __init__(self):
        self.node = level1
        self.screen = MainScreen(self.got_text)
        if self.node.background:
            self.screen.background.image = self.node.background
        self.screen.text(self.node.description)
        self.screen.run()

    def got_text(self, text):
        p = Parser(text, self.node.objects)
        new_node = self.node.do(p.match())
        if isinstance(new_node, Node):
            self.node = new_node
        elif isinstance(new_node, Game):
            game = new_node
            def exit(won=False):
                game.exit(won)
                self.screen.text(self.node.description)
                cocos.director.director.pop()

            game_obj = game.game_cls(exit)
            cocos.director.director.push(game_obj.main_scene())

        self.screen.text(self.node.description)
        if self.node.background:
            self.screen.background.image = self.node.background


def main():
    here = os.path.abspath(os.path.dirname(__file__))
    images = os.path.join(here, 'images')

    import pyglet.resource
    pyglet.resource.path = [images,
                            os.path.join(here, 'space_invader', 'graphics')]
    pyglet.resource.reindex()
    Main()


if __name__ == '__main__':
    main()
