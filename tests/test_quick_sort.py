import unittest
from algodspy.quick_sort import QuickSort


class TestQuickSort(unittest.TestCase):

    def test_sort_list(self):
        data = [3, 2, 1]
        sorter = QuickSort()
        result = sorter.sort(data)
        test = sorted(data)
        self.assertEqual(result, test)
