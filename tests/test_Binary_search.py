import unittest
from algodspy.Binary_search import BinarySearch

class TestBinarySearch(unittest.TestCase):
    def test_run_naive(self):
        data = [1, 2, 3, 4, 5]
        test = 1
        search = BinarySearch(data, 2)
        result = search.run(kind='naive')
        self.assertEqual(test, result)


    def test_run_recursive(self):
        data = [1, 2, 3, 4, 5]
        test = 1
        search = BinarySearch(data, 2)
        result = search.run(kind='recursive')
        self.assertEqual(test, result)

    def test_run_naive_no_value(self):
        data = [1, 2, 3, 4, 5]
        test = -1
        search = BinarySearch(data, 8)
        result = search.run(kind='naive')
        self.assertEqual(test, result)

    def test_run_recursive_no_value(self):
        data = [1, 2, 3, 4, 5]
        test = -1
        search = BinarySearch(data, 8)
        result = search.run(kind='recursive')
        self.assertEqual(test, result)