import unittest
from algodspy.fibonacci import Fibonacci


class TestQuickSort(unittest.TestCase):

    def test_naive(self):
        n = 1
        fib = Fibonacci()
        result = fib.run(n, 'naive')
        test = 1
        self.assertEqual(result, test)

    def test_recursive(self):
        n = 2
        fib = Fibonacci()
        result = fib.run(n, 'recursive')
        test = 1
        self.assertEqual(result, test)

    def test_memoized(self):
        n = 3
        fib = Fibonacci()
        result = fib.run(n, 'memoized')
        test = 2
        self.assertEqual(result, test)

    def test_dinamic(self):
        n = 4
        fib = Fibonacci()
        result = fib.run(n, 'dynamic')
        test = 3
        self.assertEqual(result, test)
