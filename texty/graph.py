
import random
from collections import namedtuple


Action = namedtuple('Action', ['action', 'obj'])

random_actions = [
    'Herr Katz versucht seinen eigenen Schwanz zu fangen. Dreht sich eins, zwei, unendlich im Kreis.',
    'Herr Katz stellt sich tot.Warum? Weil er es kann. ',
    'Herr Katz würde sich gerne putzen, er hat nur leider eine Katzenhaarallergie und darum niest er.',
    'Herr Katz findet es zum Kotzen. Darum kotzt er jetzt.',
    'Herr Katz schmeißt deine Tasse runter. Nastrovje!  ',
    'Herr Katz zerfetzt das Klopapier. Lustig.',
    'Herr Katz setzt sich vor die Türe und wartet bis sie aufgeht. Dann bleibt er sitzen.',
    'Herr Katz trägt jetzt Damenunterwäsche.'
]

class Game:
    def __init__(self, game_cls, exit):
        self.game_cls = game_cls
        self.exit = exit

class Node:

    def __init__(self, description, actions, objects=None, move_to=None):
        self._initial_description = self.description = description
        self.actions = actions
        self.background = None
        self.objects = objects or {}
        self.move_to = move_to or self._default_move_to

    def _default_move_to(self):
        pass

    def hilfe(self, obj):
        self.description = self._initial_description

    def do_raw_input(self, text):
        return None

    def do(self, action):
        if not action.action:
            self.description = (
                random.choice(random_actions) +
                '\n\n...\n\n' +
                self._initial_description
            )
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


class GameOverNode(Node):
    def do(self, action):
        return self


def game_over(description):
    return GameOverNode(description + '\n\nGAME OVER', actions={})
