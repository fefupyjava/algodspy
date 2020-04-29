class Grasshopper():

    def __init__(self, k):
        if k:
            self.k = k
        else:
            self.k = 2
    
    def __naive(self, n):
        F = [0] * (n + 1)
        F[0] = 1
        F[1] = 1
        for i in range(2, n + 1):
            for j in range(1, self.k + 1):
                F[i] += F[i - j]
        return F[n]

    def __recursive(self, n):
        result = 0
        cur = self.k
        if n < 2:
            return 1
        else:
            if n < cur:
                cur = n
            for i in range(1, cur + 1):
                result += self.__recursive(n - i)
        return result

    def __memoized(self, n):
        data = {0: 1, 1: 1}
        cur = self.k
        if n in data:
            return data[n]
        data[n] = 0
        if n < cur:
                cur = n
        for i in range(1, cur + 1):
            data[n] += self.__memoized(n - i)
        return data[n]
    
    def __dynamic(self, n):
        F = [0] * (n + 1)
        F[0] = 1
        F[1] = 1
        for i in range(2, n + 1):
            for j in range(1, self.k + 1):
                F[i] += F[i - j]
        return F[n]
        
    def run(self, n, kind):
        if kind == 'naive':
            return self.__naive(n)
        elif kind == 'recursive':
            return self.__recursive(n)
        elif kind == 'memoized':
            return self.__memoized(n)
        elif kind == 'dynamic':
            return self.__dynamic(n)
        else:
            return('Error') 