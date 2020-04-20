import unittest
from algodspy.quick_sort import QuickSort


class TestQuickSort(unittest.TestCase):

    def test_sort_list(self):
        data = [3, 2, 1]
        sorter = QuickSort()
        result = sorter.sort(data)
        test = sorted(data)
        self.assertEqual(result, test)

    def test_sort_list2(self):
        data = [6, 3, 9, 2, 8]
        sorter = QuickSort()
        result = sorter.sort(data)
        test = sorted(data, reversed=True)
        self.assertEqual(result, test)
