import unittest
from algodspy.tower_of_hanoi import TowerOfHanoi


class TestTowerOfHanoi(unittest.TestCase):

    def test_naive(self):
        n = 3
        hanoi = TowerOfHanoi
        result = hanoi.run(n, 'naive')
        test = 7
        self.assertEqual(result, test)

    def test_recursive(self):
        n = 1
        hanoi = TowerOfHanoi
        result = hanoi.run(n, 'recursive')
        test = 'A -> B'
        self.assertEqual(result, test)

