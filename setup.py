#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

requirements = [
    'cocos2d'
]

setup(
    name='texty',
    packages=['texty'],
    entry_points={
        'console_scripts': [
            'texty = texty.main:main'
        ]
    },
    install_requires=requirements
)
