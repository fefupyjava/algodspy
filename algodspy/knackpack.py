class Pack:
 
    def __init__(self, items):
        self.items = items
 
 
    def __naiev(self, size):
        pass
 
   
    def __recursive(self, size):
        pass
 
 
    def __memoized(self, size):
        pass
 
 
    def __dynamic(self, size):
        n = len(self.items)
        tmp = [[0 for j in range(size + 1)] for i in range(n + 1)]
        for i in range(1, n + 1):
            weight, price = self.items[i - 1]
            for j in range(1, size + 1):
                if weight > j:
                    tmp[i][j] = tmp[i - 1][j]
                else:
                    tmp[i][j] = max(tmp[i - 1][j], tmp[i - 1][j - weight] + price)
 
        answer = []
        for i in range(n, 0, -1):
            if tmp[i][size] != tmp[i - 1][size]:
                answer.append(self.items[i - 1])
                size -= self.items[i - 1][0]
 
        return answer[::-1]
 
 
    def run(self, size, kind):
        if kind == 'naive':
            pass
        elif kind == 'recursive':
            pass
        elif kind == 'memoized':
            pass
        elif kind == 'dynamic':
            return self.__dynamic(size)
        else:
            print('Неверное значение параметра kind')
            return
               
 
    def __repr__(self):
        return self.items.__repr__()
