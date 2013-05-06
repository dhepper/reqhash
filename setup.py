#!/usr/bin/env python

from setuptools import setup
import sys

with open('README.txt') as file:
    long_description = file.read()


extra = {}
if sys.version_info >= (3,):
        extra['use_2to3'] = True


setup(name='reqhash',
    version='0.1.2',
    description='Calculate a hash value over a requirement file.',
    long_description=long_description,
    author='Daniel Hepper',
    author_email='daniel@butfriendly.com',
    url='https://github.com/dhepper/reqhash',
    packages=['reqhash'],
    entry_points = {
        'console_scripts': [
            'reqhash = reqhash:main',
        ]
    },
    test_suite = 'tests',
    **extra
)
