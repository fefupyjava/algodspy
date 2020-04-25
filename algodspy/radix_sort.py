class RadixSort:

    def __init__(self):
        pass

    def sort(self, data, reverse=False):
        data_copy = data.copy()
        length = len(str(max(data_copy)))
        for i in range(length):
            b = [[] for k in range(10)]
            for x in data_copy:
                value = x // 10 ** i % 10
                b[value].append(x)
            data_copy = []
            for k in range(10):
                data_copy = data_copy + b[k]
        if reverse:
            return data_copy[::-1]
        else:
            return data_copy
