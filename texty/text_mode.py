

from texty.graph import n1, Action
from texty.parser import Parser

def main():
    n = n1
    while True:
        print('Beschreibung: '+ n.description)
        action = input('Aktion: ')
        p = Parser(action)
        n = n.do(p.match())
