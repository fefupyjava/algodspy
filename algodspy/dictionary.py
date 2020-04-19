class Dictionary:
    def __init__(self):
        self.data = {}
        
    def append(self, key, value):
        if key not in self.data:
            self.data[key] = value
    
    def value(self, key):
        return self.data.get(key)
    
    def change(self, key, value):
        if key in self.data:
            self.data[key] = value
        
    def size(self):
        return len(self.data)