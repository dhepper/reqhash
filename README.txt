reqhash
=======

Calculate a hash value over a requirement file.

reqhash parses referenced requirements and ignores changes in comments
and whitespace.

Author: Daniel Hepper <daniel@hepper.net>
License: MIT, see LICENSE.txt

Installation
------------

You can install reqhash from PyPI:

    $ pip install reqhash

Or directly from the repo:

    $ git clone https://github.com/dhepper/reqhash
    ...
    $ python setup.py install

Usage
-----

    reqhash [-h] filename

    Calculate a digest for a requirements file.

    Positional arguments:
    filename    path to requirements file

    Optional arguments:
    -h, --help  show this help message and exit

Example
-------
$ reqhash requirements.txt
302bf9e94323ec2b6ca04b76cd407602
