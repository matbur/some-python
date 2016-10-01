import unittest

from word import Word


class TestWord(unittest.TestCase):
    a = Word('a')
    aa = Word('aa')
    b = Word('b')

    def test_equal(self):
        self.assertEqual(self.a, self.a)

    def test_not_equal(self):
        self.assertNotEqual(self.a, self.aa)
