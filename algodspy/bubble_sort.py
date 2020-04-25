class BubbleSort:
    def __init__(self):
        pass

    def sort(self, data, reverse=False):
        data_copy = data.copy()
        if not reverse:
            for i in range(len(data_copy) - 1):
                for j in range(len(data_copy) - i - 1):
                    if data_copy[j] > data_copy[j + 1]:
                        data_copy[j], data_copy[j + 1] = \
                            data_copy[j + 1], data_copy[j]
            return data_copy
        if reverse:
            for i in range(len(data_copy) - 1):
                for j in range(len(data_copy) - i - 1):
                    if data_copy[j] < data_copy[j + 1]:
                        data_copy[j], data_copy[j + 1] = \
                            data_copy[j + 1], data_copy[j]
        return data_copy
