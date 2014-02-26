import unittest
from os.path import abspath, dirname, join

from clasify import get_language

TEST_PATH = join(dirname(abspath(__file__)), 'cases')


def _readfile(filename):
    filename = join(TEST_PATH, filename)
    with open(filename) as f:
        return f.read()


class ProgrammingLanguageClasifier(unittest.TestCase):
    def test_python(self):
        self.assertEqual(get_language(_readfile('python.py')), 'python')

    def test_html(self):
        self.assertEqual(get_language(_readfile('webpage.html')), 'html')

    def test_javascript(self):
        self.assertEqual(get_language(_readfile('app.js')), 'javascript')

    def test_(self):
        self.assertEqual(get_language(_readfile('git-delete-branch')), 'shell')


def main():
    unittest.main()


if __name__ == '__main__':
    main()
