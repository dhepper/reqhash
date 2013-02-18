#!/usr/bin/env python

from setuptools import setup

setup(name='reqhash',
    version='0.1',
    description='Calculate a hash value over a requirement file.',
    author='Daniel Hepper',
    author_email='daniel@butfriendly.com',
    url='https://github.com/dhepper/reqhash',
    packages=['reqhash'],
    entry_points = {
        'console_scripts': [
            'reqhash = reqhash:main',
        ]
    }
)
