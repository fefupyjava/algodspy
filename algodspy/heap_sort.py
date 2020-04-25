class HeapSort:

    def __init__(self):
        pass

    def sort(self, data, reverse=False):
        data_copy = data.copy()
        # построение кучи с конца до корня(0)
        for i in range(len(data_copy), -1, -1):
            self.heapify(data_copy, len(data_copy), i)

        # Так как корень имеет наиб.значние ставим его в конец,
        # и для оставшихся элементов находим новый корень
        for i in range(len(data_copy) - 1, 0, -1):
            data_copy[0], data_copy[i] = data_copy[i], data_copy[0]
            self.heapify(data_copy, i, 0)
        if reverse:
            return data_copy[::-1]
        else:
            return data_copy

    # heapify - функция построения двоичной кучи с помощью списка
    # Замечание - заменить рекурсивную функцию !!!
    def heapify(self, data, n, i):
        largest = i  # корень
        left = i * 2 + 1
        right = i * 2 + 2

        if left < n and data[left] > data[largest]:
            largest = left
        if right < n and data[right] > data[largest]:
            largest = right
        if largest != i:
            data[i], data[largest] = data[largest], data[i]
            self.heapify(data, n, largest)
