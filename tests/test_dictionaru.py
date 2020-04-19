import unittest
from algodspy.dictionary import Dictionary


class TestDictionary(unittest.TestCase):
    def setUp(self):
        self.data = {}
        self.dictionary = Dictionary()
        
    def test_init(self):
        self.assertEqual(self.dictionary.data, self.data)
        
    def test_append(self):
        self.dictionary.append('q', 1)
        self.data['q'] = 1
        self.assertEqual(self.dictionary.data, self.data)
        
    def test_value(self):
        self.dictionary.append('q', 1)
        self.data['q'] = 1
        self.assertEqual(self.dictionary.value('q'), self.data['q'])    
        
    def test_change(self):
        self.dictionary.append('q', 1)
        self.data['q'] = 1
        self.dictionary.change('q', 5)
        self.data['q'] = 5
        self.assertEqual(self.dictionary.data, self.data)
        
    def test_size(self):
        self.dictionary.append('q', 1)
        self.data['q'] = 1
        self.assertEqual(self.dictionary.size(), len(self.data))
    