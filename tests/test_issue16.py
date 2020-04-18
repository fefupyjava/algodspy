import unittest
from algodspy.issue16 import Dictionary

class TestDictionary(unittest.TestCase):
    def setUp(self):
        self.data = {}
        self.issue16 = Dictionary()
        
    def test_init(self):
        self.assertEqual(self.issue16.data, self.data)
        
    def test_append(self):
        self.issue16.append('q', 1)
        self.data['q'] = 1
        self.assertEqual(self.issue16.data, self.data)
        
    def test_value(self):
        self.issue16.append('q', 1)
        self.data['q'] = 1
        self.assertEqual(self.issue16.value('q'), self.data['q'])    
        
    def test_change(self):
        self.issue16.append('q', 1)
        self.data['q'] = 1
        self.issue16.change('q', 5)
        self.data['q'] = 5
        self.assertEqual(self.issue16.data, self.data)
        
    def test_size(self):
        self.issue16.append('q', 1)
        self.data['q'] = 1
        self.assertEqual(self.issue16.size(), len(list(self.data.keys())))
    