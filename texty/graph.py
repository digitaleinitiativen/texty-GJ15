
import random
from collections import namedtuple


Action = namedtuple('Action', ['action', 'obj'])

random_actions = [
    'den eigenen Schwanz fangen',
    'sich tot stellen',
    'sich putzen',
    'kotzen',
    'was runterschmeissen',
    'was zerfetzen',
    'vor die Türe setzen und warten',
    'Starren'
]


class Node:

    def __init__(self, description, actions, move_to=None):
        self._initial_description = self.description = description
        self.actions = actions
        self.background = None
        self.move_to = move_to or self._default_move_to

    def _default_move_to(self):
        pass

    def hilfe(self, obj):
        self.description = self._initial_description

    def do(self, action):
        print('Aktion: {0}'.format(action))
        if not action.action:
            self.description = random.choice(random_actions)
            return self

        if hasattr(self, action.action):
            result = getattr(self, action.action)(action.obj)
            if result:
                return result
            return self

        if action in self.actions:
            action_result  = self.actions[action]
            if isinstance(action_result, Node):
                action_result.move_to()
                return action_result
            elif callable(action_result):
                action_result(self)
                return self
        else:
            return self

def change_description(description):
    def do_change(node):
        node.description = description
    return do_change
