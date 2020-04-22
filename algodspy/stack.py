class Stack:

    def __init__(self, array):
        self.stack = array

    def append(self, value):
        return self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def __len__(self):
        return len(self.stack)

    def __str__(self):
        return f'{self.stack}'
