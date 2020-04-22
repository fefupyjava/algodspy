import unittest
from algodspy.selection_sort import SelectionSort


class TestSelectionSort(unittest.TestCase):

    def test_sort_list(self):
        data = [4, 2, 1, 67]
        sorter = SelectionSort()
        result = sorter.sort(data)
        test = sorted(data)
        self.assertEqual(result, test)

    def test_sort_list_reverse(self):
        data = [4, 2, 1, 67]
        sorter = SelectionSort()
        result = sorter.sort(data, reverse=True)
        test = sorted(data, reverse=True)
        self.assertEqual(result, test)
