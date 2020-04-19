import unittest
from algodspy.insertion_sort import InsertionSort

class TestInsertionSort(unittest.TestCase):

    def test_sort_list(self):
        data = [3, 1, 2]
        sorter = InsertionSort()
        result = sorter.sort(data)
        test = sorted(data)
        self.assertEqual(result, test)

