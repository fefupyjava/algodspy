class RadixSort:

    def __init__(self):
        pass

    def sort(self, data, reverse=False):
        data = data.copy()
        length = len(str(max(data)))
        for i in range(length):
            b = [[] for k in range(10)]
            for x in data:
                value = x // 10 ** i % 10
                b[value].append(x)
            data = []
            for k in range(10):
                data = data + b[k]
        if reverse:
            return data[::-1]
        else:
            return data
