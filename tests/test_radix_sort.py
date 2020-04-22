import unittest
from algodspy.radix_sort import RadixSort


class TestRadixSort(unittest.TestCase):

    def test_sort_list(self):
        data = [20, 15, 2, 1, 18]
        sorter = RadixSort()
        result = sorter.sort(data)
        test = sorted(data)
        self.assertEqual(result, test)

    def test_sort_list_reversed(self):
        data = [20, 15, 2, 1, 18]
        sorter = RadixSort()
        result = sorter.sort(data, True)
        test = sorted(data, reverse=True)
        self.assertEqual(result, test)
