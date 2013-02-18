#!/usr/bin/env python

import hashlib

from reqhash.parser import parse_requirements


def hash_requirements(filename):
    requirements = parse_requirements(filename)
    digest = hashlib.md5("\n".join(requirements)).hexdigest()
    return digest 


def main():
    import argparse
    argparser = argparse.ArgumentParser(description='Calculate a digest for a requirements file.')
    argparser.add_argument('filename', help='path to requirements file')
    args = argparser.parse_args()
    print hash_requirements(args.filename)


if __name__ == '__main__':
    main()
