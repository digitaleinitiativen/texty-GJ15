#!/usr/bin/env python
# -*- coding: utf-8 -*-


from texty.graph import Node, game_over


class Level(Node):
    def __init__(self):
        description = '''
Auf die Plätze, Feuer, fertig, Flamme, schlafende-Katze-wird-von-Staubsauger-überrascht-Geschwindigkeit, los! 
So war der Herr Katz also durch die zweite Klappe gebeamt. Als seine
Augen sich an das Neongeflacker gewöhnt haben, findet er sich in einem
runden Raum mit 4 Ecken wieder. In jeder eine Katzenklappe. Ein Reisebüro also. '''
        super().__init__(description,
                         actions={},
                         objects={})

    def do_raw_input(self, text):
        print(text)
        if str(text.strip()) in ('b', '5'):
            return self.next_level
        return game_over('katzenbox game over')


    def umsehen(self, obj=None):
        self.description = '''
Er starrt in das katzenhafte Gesicht einer Katze. Fräulein Travelpussy
liest er auf dem  Namensschild. Macht Sinn. Denn Fräulein
Travelpussy mag Traveling und Puzzeln. “MauMauMauMauMau” mauzt Herr Katz.
“Mau” erwidert Pussy. “Mau” sagt Herr Katz nickend.
Nachdem jetzt alles geklärt ist, nun zu den Spielregeln. Zur Auswahl stehen 4
Klappen. Doch ob er wirklich richtig geht, weiß er erst, wenn das
Funkelglitzerkatzenklappenportallicht angeht. Und Fräulein Travelpussy,
die alte Showmasterin, kennt die Antwort, macht aber einen auf Sphinx. Mahlzeit. 
Nun zum Rätsel. Eine Katze will sich auf den Mars
einschmuggeln, muss aber an einer räudigen Türsteherkatze vorbei. Er beobachtet. 
Als erstes kommt eine Katze. Räudigen Türsteherkatze sagt:"16", worauf die Katze schlicht:"8"
sagt. Dann kommt eine Katze. Räudige Türsteherkatze sagt:"28"
und Katze sagt:"14". Als eine Katze kommt, sagt räudige Türsteherkatze:"8" und bekommt als Antwort:"4". Alle dürfen passieren.
Ach so, das ist ja einfach, denkt die Katze und antwortet auf Katzes Frage:"12" lässig "6" und wird umgehend
verhaftet. Was hätte er wohl sagen müssen? a)5 b)5 c)29038 oder d)10'''

level3 = Level()
