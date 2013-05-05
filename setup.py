#!/usr/bin/env python

from setuptools import setup

with open('README.txt') as file:
    long_description = file.read()

setup(name='reqhash',
    version='0.1',
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
    test_suite = 'tests'
)
