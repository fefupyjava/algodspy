import unittest
from algodspy.bubble_sort import BubbleSort


class TestBubbleSort(unittest.TestCase):
    def test_sort_ascending(self):
        data = [2, 4, 3, 1, 5]
        test = sorted(data)
        sorter = BubbleSort()
        result = sorter.sort(data)
        self.assertEqual(result, test)

    def test_sort_decending(self):
        data = [2, 4, 3, 1, 5]
        test = sorted(data, reverse=True)
        sorter = BubbleSort()
        result = sorter.sort(data)
        self.assertEqual(result, test)