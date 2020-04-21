import unittest
from algodspy.insertion_sort import InsertionSort


class TestInsertionSort(unittest.TestCase):

    def test_sort_list(self):
        data = [3, 1, 2]
        sorter = InsertionSort()
        result = sorter.sort(data)
        test = sorted(data)
        self.assertEqual(result, test)

    def test_sort_list_reversed(self):
        data = [3, 1, 2]
        sorter = InsertionSort()
        result = sorter.sort(data, True)
        test = sorted(data, reverse=True)
        self.assertEqual(result, test)
