class SelectionSort:

    def __init__(self):
        pass

    def sort(self, data, reverse=False):
        data = data.copy()
        n = len(data)
        for i in range(n):
            m = i
            for j in range(i, n):
                if data[j] < data[m]:
                    m = j
            data[i], data[m] = data[m], data[i]
        if reverse:
            return data[::-1]
        else:
            return data

