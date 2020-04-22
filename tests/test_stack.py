import unittest
from algodspy.stack import Stack


class TestStack(unittest.TestCase):

    def setUp(self):
        self.data = [4, 3, 2]
        self.stack = Stack(self.data)

    def test_init(self):
        self.assertEqual(self.stack.data, self.data)

    def test_append(self):
        self.data.append(3)
        self.stack.append(3)
        self.assertEqual(self.stack.data, self.data)

    def test_pop(self):
        self.data.pop()
        self.stack.pop()
        self.assertEqual(self.stack.data, self.data)
    
    def test_len(self):
        self.assertEqual(len(self.stack.data), len(self.data))
