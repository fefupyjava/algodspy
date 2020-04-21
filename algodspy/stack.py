class Stack:
    def __init__(self, stack):
        self.stack = stack
    
    def append(self, value):
        return self.stack.append(value)
    
    def pop(self):
        return self.stack.pop()

    def __str__(self):
        return f'{self.stack}'

array = Stack([4, 3, 2, 15])
array.append(42)
print(array)
array.pop()
print(array)