class ListExample:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return self.data.__repr__()

    def append(self, value):
        self.data.append(value)
