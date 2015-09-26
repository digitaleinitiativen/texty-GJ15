
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
    description='''
Es war einmal vor langer Zeit, gestern, der ehrenwerte Herr Katz. Herr Katz war
ein Lauser, also nicht sonderlich verlaust, aber dafuer hatte er Lausbefall der
uebleren Sorte. Und er war etwas schwer von Begriff und auch in uebrigen
Belangen. So starrte er tagein, tagaus ins Leere, leckte sich gelegentlich
versonnen seine Eier und jagte von Zeit zu Zeit seinen eigenen Schwanz.
Erfolglos. Ja, so war er, der Herr Katz. Gestern Abend also, da saß er so in
seinem Wohnzimmer. Orientierungslos. Hoechste Zeit sich umzusehen.''',
    actions={
        Action('schnurren', None): change_description('''
Oh, dies dünkt den Herr Katz ganz annehmbar. Molback, da fängt der Seckel doch
glatt an zu schnurren. Wie praktisch, dass ihm ein Laserpointerlicht aufgeht.
'''),
        Action('umsehen', None): change_description('''
Der werte Herr Katze sieht sich um und entdeckt eine mysteriös funkelnde
Katzenklappe, ein hässliches Potpourri, eine Katzentoilette, einen Stapel
frisch gebügelter Wäsche, ein Filet auf einem geblümelten Villeroy und Boch
Teller'''),
        Action('schlafen', None): change_description('''
zzzzz, mau, zzzzz, mau, zzzzz, mau, zzzz, mau, wuff "oh I forgot how to cat",
zzzz, mau, zzzz, mau'''),
    }
)
