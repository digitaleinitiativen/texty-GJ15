#!/usr/bin/env python
# -*- coding: utf-8 -*-

from texty.graph import Node

class Level(Node):

    def __init__(self):
        description = '''
wie praktisch ein glitzerndes Portal.  So war der Herr Katz also durch die
erste Klappe gebeamt. Als seine Augen sich an das grelle Licht gewöhnt hatten
starrte er verwirrt in die glasig-ausdrucklosen Augen eines ausgebrannten
Weltraumsternstaubsaugervertreters kurz WRSSSV, welcher sich ausgerechnet mit
seiner Staubsaugerarmada russischen Herstellers made in Bängladasch vor der
nächsten Katzenklappe positoniert hatte und nicht den Anschein erweckte, als ob
er sich in diesem Lichtjahr noch bewegen würde. “Verflixt und zugenäht” denkt
sich Herr Katz und stürzt sich mit einem “Auf und drauf” ins Getümmel. 
'''
        super().__init__(description, {}, None)

    def schnurren(self, obj):
        self.description = '''
Oh, dies dünkt den Herr Katz ganz annehmbar. Molback, da fängt der Seckel doch
glatt an zu schnurren. Wie praktisch, dass ein Miniraumschiff mit Katzensitz
für ihn bereitsteht.
'''

    def umsehen(self, obj):
        self.description = '''
Der werte Herr Katze sieht sich um und entdeckt eine mysteriös funkelnde
Katzenklappe, einen Weltraumsternstaubsaugervertreter mit stockhä, eine
Staubsaugerarmada
'''

level2 = Level()
