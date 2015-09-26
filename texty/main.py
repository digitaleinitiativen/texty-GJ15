from texty.graph import n1
from texty.parser import Parser
from .screen import MainScreen


class Main():

    def __init__(self):
        self.node = n1
        self.screen = MainScreen(self.got_text)
        self.screen.text(self.node.description)
        self.screen.run()

    def got_text(self, text):
        p = Parser(text)
        self.node = self.node.do(p.match())
        self.screen.text(self.node.description)


def main():
    Main()


if __name__ == '__main__':
    main()
