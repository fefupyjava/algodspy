class InsertionSort:

    def __init__(self):
        pass

    def sort(self, data, reverse=False):
        data_copy = data.copy()
        for i in range(1, len(data_copy)):
            item = data_copy[i]
            j = i - 1
            while j >= 0 and data_copy[j] > item:
                data_copy[j + 1] = data_copy[j]
                j -= 1
            data_copy[j + 1] = item
        if reverse:
            return data_copy[::-1]
        else:
            return data_copy
