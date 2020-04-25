class SelectionSort:

    def __init__(self):
        pass

    def sort(self, data, reverse=False):
        data_copy = data.copy()
        n = len(data_copy)
        for i in range(n):
            m = i
            for j in range(i, n):
                if data_copy[j] < data_copy[m]:
                    m = j
            data_copy[i], data_copy[m] = data_copy[m], data_copy[i]
        if reverse:
            return data_copy[::-1]
        else:
            return data_copy

