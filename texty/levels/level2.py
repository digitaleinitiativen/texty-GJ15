#!/usr/bin/env python
# -*- coding: utf-8 -*-

from texty.graph import Node

class Level(Node):

    def __init__(self):
        description = '''
wie praktisch ein glitzerndes Portal. So war der Herr Katz also durch die
erste Klappe gebeamt. Als seine Augen sich an das grelle Licht gewöhnt hatten,
starrte er verwirrt in die glasig-ausdruckslosen Augen eines ausgebrannten
Weltraumsternstaubsaugervertreters kurz WRSSSV, welcher sich ausgerechnet mit
seiner Staubsaugerarmada russischen Herstellers made in Bängladasch vor der
nächsten Katzenklappe positoniert hatte und nicht den Anschein erweckte, als ob
er sich in diesem Lichtjahr noch bewegen würde. “Verflixt und zugenäht” denkt
sich Herr Katz und stürzt sich mit einem “Auf und drauf” ins Getümmel.
'''
        super().__init__(description,
                         actions={},
                         objects={
                             'miniraumschiff': []
                         })

    def spielen(self, obj=None):
        pass

    def schnurren(self, obj):
        self.description = '''
Oh, dies dünkt den Herr Katz ganz annehmbar. Molback, da fängt der Seckel doch
glatt an zu schnurren. Wie praktisch, dass ein Miniraumschiff in katzengerechter Größe
für ihn bereitsteht. Tja, Freunde, wollen wir ein Spiel spielen?
'''

    def umsehen(self, obj):
        if obj == 'miniraumschiff':
            self.description = 'Du siehst das miniraumschiff an und hast lust damit zu spielen'
        else:
            self.description = '''
    Der werte Herr Katze sieht sich um und entdeckt eine mysteriös funkelnde
    Katzenklappe, einen Weltraumsternstaubsaugervertreter mit einer
    Staubsaugerarmada, wie praktisch wäre jetzt ein wenig Inspiration...schnurr, schnurr...
    '''

level2 = Level()
