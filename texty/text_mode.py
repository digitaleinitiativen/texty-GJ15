

from texty.graph import n1, Action


def main():
    n = n1
    while True:
        print('Beschreibung: '+ n.description)
        action = input('Aktion: ')
        obj = None
        # TODO: include real parser
        if 'fisch' in action:
            obj = 'fisch'
            action = action.split(' ')[0]
        n = n.do(Action(action, obj))
