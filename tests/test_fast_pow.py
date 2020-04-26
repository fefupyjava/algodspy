import unittest
from algodspy.fast_pow import Fast_Pow


class TestFastPow(unittest.TestCase):

    def test_naive(self):
        exp = Fast_Pow(2, 5)
        result = exp.run('naive')
        test = 32
        self.assertEqual(result, test)

        exp = Fast_Pow(2, 0)
        result = exp.run('naive')
        test = 1
        self.assertEqual(result, test)

        exp = Fast_Pow(2, 1)
        result = exp.run('naive')
        test = 2
        self.assertEqual(result, test)

        exp = Fast_Pow(2, -2)
        result = exp.run('naive')
        test = 1 / 4
        self.assertEqual(result, test)

    def test_recursive(self):
        exp = Fast_Pow(3, 4)
        result = exp.run('recursive')
        test = 81
        self.assertEqual(result, test)

        exp = Fast_Pow(3, 0)
        result = exp.run('recursive')
        test = 1
        self.assertEqual(result, test)

        exp = Fast_Pow(3, 1)
        result = exp.run('recursive')
        test = 3
        self.assertEqual(result, test)

        exp = Fast_Pow(3, -4)
        result = exp.run('recursive')
        test = 1 / 81
        self.assertEqual(result, test)