class InsertionSort:

    def __init__(self):
        pass

    def sort(self, data, reverse=False):
        data = data.copy()
        for i in range(1, len(data)):
            item = data[i]
            j = i - 1
            while j >= 0 and data[j] > item:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = item
        if reverse:
            return data[::-1]
        else:
            return data
