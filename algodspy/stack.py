class Stack:

    def __init__(self, array=None):
        self.data = [] if not array else array 

    def append(self, value):
        return self.data.append(value)

    def pop(self):
        return self.data.pop() if self.data else None

    def __len__(self):
        return self.data.__len__()

    def __repr__(self):
        return self.data.__repr__()
