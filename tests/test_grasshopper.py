import unittest
from algodspy.grasshopper import Grasshopper


class TestGrasshopper(unittest.TestCase):

    def test_naive(self):
        n = 6
        cur = Grasshopper(4)
        result = cur.run(n, 'naive')
        test = 29
        self.assertEqual(result, test)

    def test_recursive(self):
        n = 6
        cur = Grasshopper(3)
        result = cur.run(n, 'recursive')
        test = 24
        self.assertEqual(result, test)

    def test_memoized(self):
        n = 5
        cur = Grasshopper(4)
        result = cur.run(n, 'memoized')
        test = 15
        self.assertEqual(result, test)

    def test_dynamic(self):
        n = 5
        cur = Grasshopper(3)
        result = cur.run(n, 'dynamic')
        test = 13
        self.assertEqual(result, test)