class SelectionSort:
    def __init__(self, array, key):
        self.array_to_sort = array
        self.key = key
    def sort(self):
        n = len(self.array_to_sort)
        for i in range(n):
            m = i
            for j in range(i, n):
                if self.key * self.array_to_sort[j] < self.key * self.array_to_sort[m]:
                    m = j
            self.array_to_sort[i], self.array_to_sort[m] = self.array_to_sort[m], self.array_to_sort[i]
        return self.array_to_sort


array = [int(i) for i in input('Введите список чисел: ').split()]
key = int(input('Введите ключ!\nПо возрастанию 1, по убыванию -1: '))

obj = SelectionSort(array, key)
s = obj.sort()

print(s)