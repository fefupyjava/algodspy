import unittest
from algodspy.heap_sort import HeapSort


class TestHeapSort(unittest.TestCase):

    def test_heap_sort_up(self):
        data = [4, 10, 3, 5, 1]
        sorted_heap_sort = HeapSort()
        sorted_heap_sort = sorted_heap_sort.sort(data)
        data = sorted(data)
        self.assertEqual(sorted_heap_sort, data)

    def test_heap_sort_down(self):
        data = [4, 10, 3, 5, 1]
        sorted_heap_sort = HeapSort()
        sorted_heap_sort = sorted_heap_sort.sort(data, True)
        data = sorted(data, reverse=True)
        self.assertEqual(sorted_heap_sort, data)
    # возможно нужен тест на большое кол-во исходных данный
    # из-за проблем питона с глубиной рекурсии
