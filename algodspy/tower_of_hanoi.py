class TowerOfHanoi:

    def __init__(self):
        pass

    def __naive(self, n):
        return 2 ** n - 1

    def __recursive(self, n, start, finish):
        if n == 1:
            print(n, start, finish)
        else:
            tmp = 6 - start - finish
            self.__recursive(n - 1, start, tmp)
            print(n, start, finish)
            self.__recursive(n - 1, tmp, finish)

    def run(self, n, kind):
        if kind == 'naive':
            return self.__naive(n)
        elif kind == 'recursive':
            return self.__recursive(n, 1, 3)
