import unittest
from LAB5_5 import f


class TestF(unittest.TestCase):
    def test_f(self):
        self.assertEqual(f(10), 5)  # add assertion here


if __name__ == '__main__':
    unittest.main()
