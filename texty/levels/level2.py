#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from texty.graph import Node, Action, Game
from texty.space_invader.space_invader import SpaceInvader


here = os.path.dirname(__file__)


class Level(Node):

    def __init__(self):
        description = '''
Wie praktisch ein Funkelglitzerkatzenklappenportal. So war der Herr Katz also durch die
erste Klappe mitten in den Milkyway gebeamt. Als seine Augen sich an das grelle Licht gewöhnt hatten,
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
        def exit(won=False):
            if won:
                self.actions[Action('beamen', 'portal')] = self.next_level
                self.actions[Action('beamen', None)] = self.next_level
                self.description = '''
        Hokus Pokus Fidibus und schon war die Milchstraße um einen WRSSSV weniger.
        Körig. Zeit weiterzuziehen, beamen, wie auch immer.'''
            else:
                self.description = 'Du hast verloren'
        return Game(
            SpaceInvader,
            exit
        )

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
