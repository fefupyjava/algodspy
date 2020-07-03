import unittest
from algodspy.factorial import Factorial


class TestTowerOfHanoi(unittest.TestCase):

    def test_naive(self):
        n = 3
        fact = Factorial()
        result = fact.run(n, 'naive')
        test = 6
        self.assertEqual(result, test)

    def test_recursive(self):
        n = 4
        fact = Factorial()
        result = fact.run(n, 'recursive')
        test = 24
        self.assertEqual(result, test)