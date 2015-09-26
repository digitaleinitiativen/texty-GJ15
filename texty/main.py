from texty.graph import n1
from texty.parser import Parser
from .screen import MainScreen


class Main():

    def __init__(self):
        self.node = n1
        s = MainScreen(self.got_text)
        s.text(self.node.description)
        s.run()

    def got_text(self, text):
        p = Parser(text)
        self.node = self.node.do(p.match())


def main():
    Main()


if __name__ == '__main__':
    main()
