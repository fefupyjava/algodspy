class Selection_sort:
    def __init__(self, array):
        self.array = array
    def sort(self, reverse=False):
        sign = 1 if not reverse else -1
        n = len(self.array)
        for i in range(n):
            m = i
            for j in range(i, n):
                if sign * self.array[j] < sign * self.array[m]:
                    m = j
            self.array[i], self.array[m] = self.array[m], self.array[i]
        return self.array
