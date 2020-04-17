class Queue:

    # Очередь выглядит так [end(конец очереди), ..., start(начало очереди)]
    def __init__(self):
        self.data = []

    def enqueue(self, data):
        self.data.insert(0, data)

    def dequeue(self):
        return self.data.pop()

    def size(self):
        return len(self.data)

