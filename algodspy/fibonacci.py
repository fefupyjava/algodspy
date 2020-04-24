class Fibonacci():

    def __init__(self):
        pass

    def __naive(self, n):
        if n > 0:
            fib1 = fib2 = 1
            for _ in range(n - 2):
                fib_sum = fib1 + fib2
                fib1 = fib2
                fib2 = fib_sum
            return fib2

    def __recursive(self, n):
        if n > 0:
            if n < 3:
                return 1
            return self.__recursive(n - 1) + self.__recursive(n - 2)

    def __memoized(self, n):
        fib = {0: 0, 1: 1}
        if n in fib:
            return fib[n]
        fib[n] = self.__memoized(n - 1) + self.__memoized(n - 2)
        return fib[n]

    def __dynamic(self, n):
        if n > 0:
            fib1 = 0
            fib2 = 1
            for _ in range(n):
                fib1, fib2 = fib2, fib1 + fib2
            return fib1

    def run(self, n, kind):
        if kind == 'naive':
            return self.__naive(n)
        elif kind == 'recursive':
            return self.__recursive(n)
        elif kind == 'memoized':
            return self.__memoized(n)
        elif kind == 'dynamic':
            return self.__dynamic(n)
