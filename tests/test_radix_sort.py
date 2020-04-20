import unittest
from algodspy.radix_sort import RadixSort


class TestRadixSort(unittest.TestCase):

    def test_sort_list(self):
        data = [20, 15, 2]
        sorter = RadixSort()
        result = sorter.sort(data)
        test = sorted(data)
        self.assertEqual(result, test)