#!/usr/bin/env python
# -*- coding: utf-8 -*-

from texty.graph import game_over
from .level1 import level1
from .level2 import level2
from .level3 import level3
from .level4 import level4
from .level5 import level5

level1.next_level = level2
level2.next_level = level3
level3.next_level = level4
level4.next_level = level5
level5.next_level = game_over('Gewonnen')
