class TowerOfHanoi:

    def __init__(self):
        pass

    def __naive(self, n):
        return  2 ** n - 1

    def __recursive(self, n, a, b, c):
        if n >= 1:
            self.__recursive(n - 1, a, c, b)
            print(a, "->", c)
            self.__recursive(n - 1, b, a, c)


def run(self, n, kind):
    if kind == 'naive':
        return self.__naive(n)
    elif kind == 'recursive':
        return self.__recursive(n, "A", "B", "C")
