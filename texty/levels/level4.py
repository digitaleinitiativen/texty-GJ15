
from texty.graph import Node, Action

class Level(Node):
    def __init__(self):
        self.look_around = '''
Leider nichts zu sehen, ganz schön dunkel hier. Tja, wenn die Herrschaften
glauben, dass Katzen ja eh nachtsichtig sind, dann habt ihr recht. Aber das
bringt Dich jetzt auch nicht weiter, unser Spiel, unsere Regeln. Auch Herr Katz
weiß nicht weiter und macht, was er immer macht, wenn er nicht weiter weiß.'''
        description = self.look_around
        super().__init__(description,
                         actions={},
                         objects={
                             'flagge': [],
                             'tafel': [],
                             'planet': [],
                         })

    def schnurren(self, obj=None):
        self.description = '''
Schon der alte liebe Gott sagte: Es werde xxx
'''

    def lesen(self, obj=None):
        if obj and obj == 'tafel':
            self.description = '''
Apropos Pluto, kanntet ihr den schon: Liebe Mama, Deine Mutter dachte ich wäre
groß genug... mfg Pluto'''
        else:
            self.description = 'Was will er lesen?'

    def pumpen(self, obj=None):
        if obj and obj == 'planet':
            self.description = '''
Ist ja kein Geheimnis, das Onlinepetitionen für die katz sind. Daher do it
youself und mach es zu deinem Projekt. Pumpen bis der Pluto wieder ein Planet
ist.'''
            self.actions[Action('beamen', 'portal')] = self.next_level
            self.actions[Action('beamen', None)] = self.next_level
        else:
            self.description = 'Was pumpt er auf?'

    def hissen(self, obj=None):
        if obj and obj == 'flagge':
            self.description = 'Eine Katzenflagge hissen, weil ers kann.'
            self.actions[Action('beamen', 'portal')] = self.next_level
            self.actions[Action('beamen', None)] = self.next_level
        else:
            self.description = 'Was hisst er?'

    def pissen(self, obj=None):
        self.description = '''
Augen zu, ja, auch Herr Katz braucht etwas Privatsphäre, wenn es ihm nach 5
Minuten für kleine Königskätzchen verlangt.
'''

    def licht(self, obj=None):
        self.description = '''
Magic! Zeit sich umzusehen. Da wäre eine Katzentoilette für Königskatzen und
Königskätzchen und Babykätzchen, eine Amerikaflagge, eine Tafel, eine Pumpe und
ein Funkelglitzerkatzenklappentor.
'''
        self.lights_on = True

    def umsehen(self, obj=None):
        if self.lights_on:
            self.description = '''
Da ist Herr Katz doch tatsächlich auf dem Möchte-Gern-Planeten-Pluto gelandet.
Etwas Mitleid hat er schon, mit dem Kerlchen, wo er doch jahrelang mit den
seinen Freunden Mars, Jupiter und Co. spielen durfte, wurde er doch Tatsache
wahr wieder zu Mond und so gesteckt. Man müsste eine Demo machen, oder eine
Gegendemo, oder eine Onlinepetition starten, das kann man doch nicht machen,
einfach so. Und während Herr Katz so mitleidet, güggselt er durch den Raum. Und
wie er sich so vorgestellt hatte, entdeckt er eine Fahrradpumpe zum pumpen, ein
Plakat zum Lesen, eine Amerikaflagge zum Hissen und ein Katzenklo zum... naja,
du schon wissen.
'''
        else:
            self.description = self.look_around



level4 = Level()
