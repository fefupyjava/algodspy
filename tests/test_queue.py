import unittest
from algodspy.queue import Queue


class TestQueue(unittest.TestCase):

    def setUp(self):
        self.data = []
        self.queue = Queue()

    def test_init(self):
        self.assertEqual(self.queue.data, self.data)

    def test_enqueue(self):
        self.assertEqual(self.queue.__enqueue__(1), self.data.insert(0, 1))

    def test_dequeue(self):
        self.data.append(1)
        self.queue.__enqueue__(1)
        self.assertEqual(self.queue.__dequeue__(), self.data.pop())

    def test_size(self):
        self.data.append(2)
        self.queue.__enqueue__("word")
        self.assertEqual(self.queue.__size__(), len(self.data))


