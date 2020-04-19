import unittest
from algodspy.heap_sort import HeapSort


class TestHeapSort(unittest.TestCase):

    def setUp(self):
        pass

    def test_heap_sort_up(self):
        data = [4, 10, 3, 5, 1]
        self.sorted_heap_sort = HeapSort()
        self.sorted_heap_sort = self.sorted_heap_sort.sort(data)
        self.data = sorted(data)
        self.assertEqual(self.sorted_heap_sort, self.data)

    def test_heap_sort_down(self):
        data = [4, 10, 3, 5, 1]
        self.sorted_heap_sort = HeapSort()
        self.sorted_heap_sort = self.sorted_heap_sort.sort(data, True)
        self.data = sorted(data, reverse=True)
        self.assertEqual(self.sorted_heap_sort, self.data)
    # возможно нужен тест на большое кол-во исходных данный
    # з-за проблем питона с глубиной рекурсии
