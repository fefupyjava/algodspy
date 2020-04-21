class SelectionSort:
    def __init__(self, array):
        self.array_to_sort = array
    def sort(self, reverse=False):
        sign = 1 if reverse == False else -1
        n = len(self.array_to_sort)
        for i in range(n):
            m = i
            for j in range(i, n):
                if sign * self.array_to_sort[j] < sign * self.array_to_sort[m]:
                    m = j
            self.array_to_sort[i], self.array_to_sort[m] = self.array_to_sort[m], self.array_to_sort[i]
        return self.array_to_sort


array = [4, 3, 5, 21, 43, 0, 23, 22]
obj = SelectionSort(array)
s = obj.sort(reverse=True)

print(s)