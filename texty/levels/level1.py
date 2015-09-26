#!/usr/bin/env python
# -*- coding: utf-8 -*-

from texty.graph import Node, Action, change_description, game_over


class Level(Node):
    def __init__(self, description, actions):
        super().__init__(description,
                         actions,
                         objects={
                             'filet': [],
                             'katzenklappe': [],
                             'katzentoilette': [],
                             'wäsche': []
                         })
        self.background = 'level1.jpg'

    def umsehen(self, obj=None):
        if not obj:
            self.description = '''
Der werte Herr Katz sieht sich um und entdeckt eine mysteriös funkelnde
Katzenklappe, ein hässliches Potpourri, eine Katzentoilette, einen Stapel
frisch gebügelter Wäsche und ein well-done Filet auf einem geblümelten Villeroy und Boch
Teller.'''
        else:
            self.description = ('Herr Katz starrt {0} an und starrt, und starrt, und starrt.'
                                'Und wird hungrig'.format(obj))

    def schnurren(self, obj=None):
        self.description = '''
Oh, dies dünkt den Herr Katz ganz annehmbar. Molback, da fängt der Seckel doch
glatt an zu schnurren. Aber leider hat er immer noch Hunger.
'''

    def fressen(self, obj):
        if not obj:
            self.description = 'Herr Katz muss sich noch immer entscheiden was er fressen will.'
            return
        if obj == 'filet':
            self.description = '''
nomnomnomnomnomnomnomnom, ploetzlich, ein greller Blitz am Himmel, ein
flammender Meteor stuertzt zurueck aus der Zukunft zur Erde, da stand er, der
Leibhaftige, der einzig wahre Herr Katz. Zurueckgekehrt aus der Zukunft um sich
selbst vor der Kastration zu retten. "Miau, sagt der Gegenwarts Herr Katz"
"Salve du Stricher" sag der Zukunfts Herr Katz, "Woher kommst denn du" sagt der
Gegenwarts Herr Katz, "aus der Zukunft" sagt der Zukunfts Herr Katz "Mau" sagt
der Gegenwarts Herr Katz "Mau" sagt der Zukunfts Herr Katz "Ja wo sind denn deine
Eier, ja wo sind sie denn, ja wo, ja wo sind sie denn?" fragt der Gegenwarts
Herr Katz "weg" antwortet der Zukunfts Herr Katz "Warum?" sagt der Gegenwarts
Herr Katz "Hinweis: Filet am Vorabend + Tierarzt + Morgen = ?" "Mau" sagt der
Gegenwarts Herr Katz, der die Weisheit wirklich nicht mit dem Löffel gefresssen
hat" "Ich bin dein Zukunfts Ich, gekommen aus der Zukunft, um dich davor zu
bewahren morgen entmannt zu werden" sagt der Zukunfts Herr Katz "Wie
aufmerksam" sagt der Gegenwarts Herr Katz "Flieht ihr Narren! Am besten durch
glitzerne Katzenklappen" sagt der Zukunfts Herr Katz und
verschwindet in einer dicken, nach Fisch stinkenden Rauchwolke. Egal, denkt sich Herr Katz, 
denn das einzige was zählt ist: "Was würde Spock aus Raumschiff Enterprise jetzt tun? 

    '''
            self.actions[Action('beamen', 'portal')] = self.next_level
            self.actions[Action('beamen', None)] = self.next_level
        else:
            return game_over('Herr Katz frisst {0} und stirbt daran...elendig.'.format(obj))


level1 = Level(
    description='''
Es war einmal vor langer Zeit, gestern, der ehrenwerte Herr Katz. Herr Katz war
ein Lauser, nicht sonderlich verlaust, dafür hatte er Lausbefall der
übleren Sorte. Und er war etwas schwer von Begriff. Also eigentlich strohdumm.
So starrte er tagein, tagaus ins Leere, leckte sich gelegentlich
versonnen seine Eier, schlief vor sich hin, fraß alles und jagte von Zeit zu Zeit seinen eigenen Schwanz.
Erfolglos. Wenn er keinen Plan hat, also nicht mehr weiter weiß, dann schnurrt Herr Katz.
Ja, so ist er, der Herr Katz. Gestern Abend also, da saß er so in
seinem Wohnzimmer. Orientierungslos. Höchste Zeit sich umzuschauen.''',
    actions={
        Action('schlafen', None): change_description('''
zzzzz, mau, zzzzz, mau, zzzzz, mau, zzzz, mau, wuff "oh I forgot how to cat",
zzzz, mau, zzzz, mau'''),
    }
)
