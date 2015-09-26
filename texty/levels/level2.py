#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from texty.graph import Node
from subprocess import Popen


here = os.path.dirname(__file__)


class Level(Node):

    def __init__(self):
        description = '''
Wie praktisch ein Funkelglitzerkatzenklappenportal. So war der Herr Katz also durch die
erste Klappe gebeamt. Als seine Augen sich an das grelle Licht gewöhnt hatten,
starrte er verwirrt in die glasig-ausdruckslosen Augen eines ausgebrannten
Weltraumsternstaubsaugervertreters kurz WRSSSV, welcher sich ausgerechnet mit
seiner Staubsaugerarmada russischen Herstellers made in Bängladasch vor der
nächsten Funkelglitzerkatzenklappenportal positoniert hatte und nicht den Anschein erweckte, als ob
er sich in diesem Lichtjahr noch bewegen würde. “Verflixt und zugenäht” denkt
sich Herr Katz und stürzt sich mit einem “Auf und Drauf” ins Getümmel als er das Miniraumschiff entdeckt.
'''
        super().__init__(description,
                         actions={},
                         objects={
                             'miniraumschiff': [],
                             'katzenklappe': []
                         })
        self.background = 'level2.png'

    def spielen(self, obj=None):
        space_invaders = os.path.join(here, '..', 'space_invader')
        p = Popen([sys.executable, 'space_invader.py'], cwd=space_invaders)
        p.wait()

    def schnurren(self, obj):
        self.description = '''
Oh, dies dünkt den Herr Katz ganz annehmbar. Molback, da fängt der Seckel doch
glatt an zu schnurren. Wie praktisch, dass ein Miniraumschiff in katzengerechter Größe
für ihn bereitsteht. Tja, Freunde, wollen wir ein Spiel spielen?
'''

    def umsehen(self, obj):
        if obj == 'miniraumschiff':
            self.description = 'Herr Katz sieht das miniraumschiff an und hat tierisch Lust damit zu spielen'
        elif obj == 'katzenklappe':
            self.description = '''So ein Pech aber auch, Herr Katz kommst leider nicht an das Funkelglitzerkatzenklappenportal
            heran, weil ein Weltraumsternstaubsaugervertreter mit seiner
            Staubsaugeramada davor steht.'''
        else:
            self.description = '''
    Der werte Herr Katze sieht sich um und entdeckt eine mysteriös funkelnde
    Katzenklappe, einen Weltraumsternstaubsaugervertreter mit einer
    Staubsaugerarmada, wie praktisch wäre jetzt ein wenig Inspiration...schnurr, schnurr...
    '''

level2 = Level()
