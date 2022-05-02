# coding: utf-8
from hstest.stage_test import StageTest
from hstest.test_case import SimpleTestCase


class RegexTest(StageTest):
    m_cases = [
        ("a", "a",          "True",     "Two identical patterns should return True!"),
        ("a", "b",          "False",    "Two different patterns should not return True!"),
        ("7", "7",          "True",     "Two identical patterns should return True!"),
        ("6", "7",          "False",    "Two different patterns should not return True!"),
        (".", "a",          "True",     "Don't forget that '.' is a wild-card that matches any single character."),
        ("a", ".",          "False",    "A period in the input string is still a literal!"),
        ("", "a",           "True",     "An empty regex always returns True!"),
        ("", "",            "True",     "An empty regex always returns True!"),
        ("a", "",           "False",    "A non-empty regex and an empty input string always returns False!")
    ]


    def generate(self):
        return [
            SimpleTestCase(
                stdin="{0}|{1}".format(regex, text),
                stdout=output,
                feedback=fb
            ) for regex, text, output, fb in self.m_cases
        ]


if __name__ == '__main__':
    RegexTest('regex.regex').run_tests()
