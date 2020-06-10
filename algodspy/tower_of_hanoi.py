class TowerOfHanoi:

    def __init__(self):
        pass

    def __naive(self, n):
        return 2 ** n - 1

    def __recursive(self, n, start, finish):
        if n == 1:
            lst = [n, start, finish]
            hanoi.append(lst)
        else:
            tmp = 6 - start - finish
            self.__recursive(n - 1, start, tmp)
            lst = [n, start, finish]
            hanoi.append(lst)
            self.__recursive(n - 1, tmp, finish)
        return hanoi

    def run(self, n, kind):
        if kind == 'naive':
            return self.__naive(n)
        if kind == 'recursive':

            return self.__recursive(n, 1, 3)

hanoi = []
