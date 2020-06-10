import unittest
from algodspy.tower_of_hanoi import TowerOfHanoi


class TestTowerOfHanoi(unittest.TestCase):

    def test_naive(self):
        n = 3
        hanoi = TowerOfHanoi()
        result = hanoi.run(n, 'naive')
        test = 7
        self.assertEqual(result, test)

    def test_recursive(self):
        n = 3
        hanoi = TowerOfHanoi()
        result = hanoi.run(n, 'recursive')
        test = [[1, 1, 3], [2, 1, 2], [1, 3, 2], [3, 1, 3], [1, 2, 1], [2, 2, 3], [1, 1, 3]]
        self.assertEqual(result, test)