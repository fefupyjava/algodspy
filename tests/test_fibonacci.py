import unittest
from algodspy.fibonacci import Fibonacci


class TestQuickSort(unittest.TestCase):

    def test_sort_list_naive(self):
        n = 1
        fib = Fibonacci()
        result = fib.run(n, 'naive')
        test = 1
        self.assertEqual(result, test)

    def test_sort_list_recursive(self):
        n = 2
        fib = Fibonacci()
        result = fib.run(n, 'recursive')
        test = 1
        self.assertEqual(result, test)

    def test_sort_list_memoized(self):
        n = 3
        fib = Fibonacci()
        result = fib.run(n, 'memoized')
        test = 2
        self.assertEqual(result, test)

    def test_sort_list_dinamic(self):
        n = 4
        fib = Fibonacci()
        result = fib.run(n, 'dinamic')
        test = 3
        self.assertEqual(result, test)
