import unittest
from algodspy.bucket_sort import BucketSort


class TestBucketSort(unittest.TestCase):

    def test_sort_list(self):
        alist = [3, 11, 2, 17]
        sorter = BucketSort()
        result = sorter.bucket_sort(alist)
        test = sorted(alist)
        self.assertEqual(result, test)

    def test_sort_list_reverse(self):
        alist = [4, 15, 3, 17]
        sorter = BucketSort()
        result = sorter.bucket_sort(alist, reverse=True)
        test = sorted(alist, reverse=True)
        self.assertEqual(result, test)