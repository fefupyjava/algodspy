class BubbleSort:
    def __init__(self):
        pass

    def sort(self, data, reverse=False):
        if not reverse:
            for i in range(len(data) - 1):
                for j in range(len(data) - i - 1):
                    if data[j] > data[j + 1]:
                        data[j], data[j + 1] = data[j + 1], data[j]
            return data
        if reverse:
            for i in range(len(data) - 1):
                for j in range(len(data) - i - 1):
                    if data[j] < data[j + 1]:
                        data[j], data[j + 1] = data[j + 1], data[j]
        return data


data = [2, 1, 3, 4, 5]
BubbleSort.sort(1,data, reverse=False)
print(data)