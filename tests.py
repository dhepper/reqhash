import os
import unittest

import parser

class RequirementsParserTest(unittest.TestCase):

    fixture_path =  os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fixtures')

    def test_parse_simple_requirements(self):
        pass

    def test_normalize(self):
        reqs_path = self.open_fixture('simple.txt')
        reqs_w_comments_path = self.open_fixture('simple_w_comments.txt')
        with file(reqs_path) as reqs:
            with file(reqs_w_comments_path) as reqs_w_comments:
                normalized = parser.normalize_reqs(reqs)
                normalized_w_comments = parser.normalize_reqs(reqs_w_comments)
                self.assertEqual(normalized, normalized_w_comments)

    def open_fixture(self, name):
        return os.path.join(self.fixture_path, name)

