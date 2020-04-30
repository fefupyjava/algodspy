import unittest
from algodspy.Binary_search import BinarySearch

class TestBinarySearch(unittest.TestCase):
    def test_run_naive(self):
        data = [1, 2, 3, 4, 5]
        test = 1
        search = BinarySearch()
        result = search.run(data, 2, kind='naive')
        self.assertEqual(test, result)


    def test_run_recursive(self):
        data = [1, 2, 3, 4, 5]
        test = 1
        search = BinarySearch()
        result = search.run(data, 2, kind='recursive')
        self.assertEqual(test, result)

    def test_run_naive_no_value(self):
        data = [1, 2, 3, 4, 5]
        test = -1
        search = BinarySearch()
        result = search.run(data, 8, kind='naive')
        self.assertEqual(test, result)

    def test_run_recursive_no_value(self):
        data = [1, 2, 3, 4, 5]
        test = -1
        search = BinarySearch()
        result = search.run(data, 8, kind='recursive')
        self.assertEqual(test, result)