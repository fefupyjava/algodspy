class Dictionary:
    def __init__(self):
        self.data = {}
        
    def append(self, key, value):
        if self.data.get(key) == None:
            self.data[key] = value
    
    def value(self, key):
        return self.data.get(key)
    
    def change(self, key, value):
        if self.data.get(key):
            self.data[key] = value
        
    def size(self):
        return len(self.data)