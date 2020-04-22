class RadixSort:

    def __init__(self):
        pass

    def sort(self, data, reverse=False):
        length = len(str(max(data)))
        for i in range(length):
            B = [[] for k in range(10)]
            for x in data:
                value = x // 10 ** i % 10
                B[value].append(x)
            data = []
            for k in range(10):
                data = data + B[k]
        if reverse:
            return data[::-1]
        else:
            return data