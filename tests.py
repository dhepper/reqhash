import json
import os
import unittest

from reqhash import parser

class RequirementsParserTest(unittest.TestCase):

    fixture_path =  os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fixtures')

    def test_normalize(self):
        reqs_path = self.get_fixture('simple')
        reqs_w_comments_path = self.get_fixture('simple_w_comments')
        with file(reqs_path) as reqs:
            with file(reqs_w_comments_path) as reqs_w_comments:
                normalized = parser.normalize_reqs(reqs)
                normalized_w_comments = parser.normalize_reqs(reqs_w_comments)
                self.assertEqual(normalized, normalized_w_comments)

    def test_parse_simple(self):
        reqs_path, expected = self.get_testset('simple')
        reqs = parser.parse_requirements(reqs_path)
        self.assertEquals(reqs, expected)

    def test_parse_nested(self):
        reqs_path, expected = self.get_testset('nested')
        reqs = parser.parse_requirements(reqs_path)
        self.assertEquals(reqs, expected)

    def test_normalize_inline(self):
        reqs_path = self.get_fixture('simple')
        reqs_w_inline_comments_path = self.get_fixture('simple_w_inline_comments')
        with file(reqs_path) as reqs, file(reqs_w_inline_comments_path) as reqs_w_inline_comments:
            normalized = parser.normalize_reqs(reqs)
            normalized_w_inline_comments = parser.normalize_reqs(reqs_w_inline_comments)
            self.assertEqual(normalized, normalized_w_inline_comments)

    def get_fixture(self, name):
        return os.path.join(self.fixture_path, name + '.txt')

    def get_testset(self, name):
        basename = os.path.join(self.fixture_path, name)
        reqs_path = self.get_fixture(name)
        expected_path = basename + '.json'
        with file(expected_path) as expected_file:
            expected = json.load(expected_file)
        return reqs_path, expected


