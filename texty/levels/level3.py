#!/usr/bin/env python
# -*- coding: utf-8 -*-


from texty.graph import Node


class Level(Node):
    def __init__(self):
        description = '''
auf die Plaetze, Feuer, fertig, Flamme, schlafende Katze-wird-von-Staubsauger-überrascht-Geschwindigkeit, los!'''
        super().__init__(description,
                         actions={},
                         objects={})

    def umsehen(self, obj=None):
        self.description = '''
So war der Herr Katz also durch die zweite Klappe gebeamt. Als seine
Augen sich an das grelle Licht gewöhnt haben, findet er sich in einem
runden Raum mit 4 Ecken wieder. In jeder eine Katzenklappe. Aus einem
Lautsprecher plätschern Walgesänge. An den Wänden grelle Anzeigen die
mit “5 Tage Mars, genießen sie Ihre Tage in der Sonne und lassen sie
sich nachts von atemberaubenden Laserpointershows begeistern” oder
“Aktivurlaub für die ganze Familie in der 2. Galaxie, inklusive
Wollknäulfabrikbesichtigung”. Ein Reisebüro also. In der Mitte ein
schwerer Vollholzschreibtisch. Darauf ein Laptop, mit abgenutzter Maus
und starrt in das katzenhafte Gesicht einer Katze. Fräulein Travelpussy
liest er auf dem silbernen Namensschild. Macht Sinn. Denn Fräulein
Travelpussy mag Traveling und Puzzeln. Von Beruf ist sie Travelagentin.
“MauMauMauMauMau” mauzt Herr Katz, sichtlich angetan von der Pussy.
“Mau” erwidert Pussy. “Mau” sagt Herr Katz verständnisvoll nickend.
Nachdem jetzt alles geklärt ist, nun zu den Spielregeln, für all jene
von euch, die kein spacekatzisch sprechen.  Zur Auswahl stehen 4
Klappen. Doch ob er wirklich richtig geht, weiß er erst, wenn das
Funkelglitzerkatzenklappenportallicht angeht. Und Fräulein Travelpussy,
die alte Showmasterin, macht einen auf Sphinx. Mahlzeit. Trotzdem muss
Herr Katz das Rätsel lösen.  Eine Katze will sich auf den Mars
einschmuggeln, muss aber an einer räudig aussehenden “Du kommst hier
net rein” Katze vorbei. Da er das Passierwort nicht weiß, beobachtet er
andere, wie sie das Tor passieren. Als erstes kommt eine Katze. “Du
kommst hier net rein” Katze sagt:"16", worauf die Katze schlicht:"8"
sagt. Dann kommt eine Katze. “Du kommst hier net rein” Katze sagt:"28"
und Katze sagt:"14". Als eine Katze kommt, sagt “Du kommst hier net
rein” Katze :"8" und bekommt als Antwort:"4". Alle dürfen passieren.
Ach so, das ist ja einfach, denkt die Katze und antwortet auf des “Du
kommst hier net rein” Katzes Frage:"12" lässig "6" und wird umgehend
verhaftet. Was hätte er wohl sagen müssen?'''

level3 = Level()
