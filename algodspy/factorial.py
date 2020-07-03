class Factorial:

    def __init__(self):
        pass

    def __naive(self, n):
        fact = 1
        for i in range(2, n + 1):
            fact = fact * i
        return fact

    def __recursive(self, n):
        if n == 0:
            return 1
        return self.__recursive(n - 1) * n

    def run(self, n, kind):
        if kind == 'naive':
            return self.__naive(n)
        if kind == 'recursive':
            return self.__recursive(n)