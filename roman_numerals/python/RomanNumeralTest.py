import unittest

from Roman2Decimal import parse


class MyTestCase(unittest.TestCase):
    def test_One(self):
        self.assertEqual(parse("I"), 1)

    def test_Two(self):
        self.assertEqual(parse("II"), 2)

    def test_Three(self):
        self.assertEqual(parse("III"), 3)

    def test_Four(self):
        self.assertEqual(parse("IIII"), 4)


if __name__ == '__main__':
    unittest.main()
