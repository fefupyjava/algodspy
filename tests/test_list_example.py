import unittest
from algodspy.list_example import ListExample


class TestListExample(unittest.TestCase):
    def setUp(self):
        self.data = [1, 2, 3]
        self.lst = ListExample(self.data)

    def test_list_init(self):
        self.assertEqual(self.lst.data, self.data)

    def test_list_repr(self):
        self.assertEqual(self.lst.__repr__(), self.data.__repr__())
