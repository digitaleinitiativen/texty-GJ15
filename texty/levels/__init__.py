#!/usr/bin/env python
# -*- coding: utf-8 -*-

from texty.graph import game_over
from .level1 import level1
from .level2 import level2

level1.next_level = level2
level2.next_level = game_over('Gewonnen')
