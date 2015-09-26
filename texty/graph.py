
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
        if not action or not action.action:
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
    description='',
    actions={
        Action('schnurren', None): n3
    }
)


class N1(Node):
    def __init__(self, description, actions, move_to=None):
        super().__init__(description, actions, move_to)

    def schnurren(self, obj=None):
        self.description = '''
Oh, dies dünkt den Herr Katz ganz annehmbar. Molback, da fängt der Seckel doch
glatt an zu schnurren. Wie praktisch, dass ihm ein Laserpointerlicht aufgeht.
'''

    def _activate_portal(self, obj):
        self.actions[Action('beamen', 'Portal')] = n2
        self.description = 'wie praktisch ein glitzerndes Portal.'

    def fressen(self, obj):
        if obj == 'filet':
            self.description = '''
nomnomnomnomnomnomnomnom, ploetzlich, ein greller Blitz am Himmel, ein
flammender Meteor stuertzt zurueck aus der Zukunft zur Erde, da stand er, der
Leibhaftige, der einzig wahre Herr Katz. Zurueckgekehrt aus der Zukunft um sich
selbst vor der Kastration zu retten. "Miau, sagt der Gegenwarts Herr Katz"
"Salve du Stricher" sag der Zukunfts Herr Katz, "Woher kommst denn du" sagt der
Gegenwarts Herr Katz, "aus der Zukunft" sagt der Zukunfts Herr Katz "Mau" sagt
der Gegenwarts Herr Katz "Mau" sagt der Zukunfts Herr Katz "Ja wo sind denn
Eier, ja wo sind sie denn, ja wo, ja wo sind sie denn?" fragt der Gegenwarts
Herr Katz "weg" antwortet der Zukunfts Herr Katz "Warum" sagt der Gegenwarts
Herr Katz "Hinweis: Filet am Vorabend + Tierarzt + Morgen = ?" "Mau" sagt der
Gegenwarts Herr Katz, der die Weisheit wirklich nicht mit dem Löffel gefresssen
hat" "Ich bin den Zukunfts Ich, gekommen aus der Zukunft, um dich davor zu
bewahren morgen kastriert zu werden" sagt der Zukunfts Herr Katz "Wie
aufmerksam" sagt der Gegenwarts Herr Katz "Flieht ihr Narren! Am besten durch
glitzerne Katzenklappen Wink mit dem Zaunpfal" sagt der Zukunfts Herr Katz und
verschwindet in einer dicken, nach Fisch stinkenden Rauchwolke.
    '''
            self.actions[Action('aktivieren', 'Portal')] = self._activate_portal


n1 = N1(
    description='''
Es war einmal vor langer Zeit, gestern, der ehrenwerte Herr Katz. Herr Katz war
ein Lauser, also nicht sonderlich verlaust, aber dafuer hatte er Lausbefall der
uebleren Sorte. Und er war etwas schwer von Begriff und auch in uebrigen
Belangen. So starrte er tagein, tagaus ins Leere, leckte sich gelegentlich
versonnen seine Eier und jagte von Zeit zu Zeit seinen eigenen Schwanz.
Erfolglos. Ja, so war er, der Herr Katz. Gestern Abend also, da saß er so in
seinem Wohnzimmer. Orientierungslos. Hoechste Zeit sich umzusehen.''',
    actions={
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
