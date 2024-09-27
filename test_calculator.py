import unittest
from calculator import add, substract

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_substract(self):
        self.assertEqual(substract(5, 3), 2)

if __name__ = "__main__":
    unittest.main()

