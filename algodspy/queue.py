class Queue:

    # Очередь выглядит так [end(конец очереди), ..., start(начало очереди)]
    def __init__(self):
        self.data = []

    def __enqueue__(self, data):
        self.data.insert(0, data)

    def __dequeue__(self):
        return self.data.pop()

    def __size__(self):
        return len(self.data)

