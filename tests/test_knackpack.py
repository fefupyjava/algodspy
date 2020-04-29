import unittest
from alogdspy.pack import Pack
 
 
class TestPack(unittest.TestCase):
   
    def test_naive(self):
        pass
 
    def test_memoized(self):
        pass
 
    def test_recursive(self):
        pass
 
    def test_dynamic(self):
        items = [(3, 1), (4, 6), (5, 4), (8, 7), (9, 6)]
        pack = Pack(items)
        result = pack.run(13, 'dynamic')
        test = [(8, 7), (4, 6)]
        self.assertEqual(result, test)
