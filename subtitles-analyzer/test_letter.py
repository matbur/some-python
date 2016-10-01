import unittest

from letter import Letter


class TestLetter(unittest.TestCase):
    a = Letter('a')
    b = Letter('b')
    A = Letter('A')

    def test_equal(self):
        self.assertEqual(self.a, self.a)
        self.assertEqual(self.A, self.A)

    def test_not_equal(self):
        self.assertNotEqual(self.a, self.b)
        self.assertNotEqual(self.a, self.A)

    def test_greater(self):
        self.assertGreater(self.a, self.A)
        self.assertGreater(self.b, self.a)
