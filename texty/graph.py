
import sys

from collections import namedtuple


Action = namedtuple('Action', ['action', 'obj'])


class Node:
    def __init__(self, description, actions, move_to=None):
        self.description = description
        self.actions = actions
        self.move_to = move_to or self._default_move_to

    def _default_move_to(self):
        pass

    def do(self, action):
        print('Aktion: {0}'.format(action))
        if action in self.actions:
            next_node = self.actions[action]
            next_node.move_to()
            return next_node
        else:
            return self


node_game_over = Node(
    description='Du stirbst',
    actions={},
    move_to=sys.exit
)

n3 = Node(
    description='Game Over',
    actions={},
    move_to=sys.exit
)


n2 = Node(
    description='Das essen schmeckt gut',
    actions={
        Action('schnurren', None): n3
    }
)

n1 = Node(
    description=('Du siehst ein Gummiball und ein Fisch.\n'
                 'Was tust du?'),
    actions={
        Action('fressen', 'gummiball'): node_game_over,
        Action('fressen', 'fisch'): n2
    }
)
