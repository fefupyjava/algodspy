import random
from functools import reduce


class RadixSort:

    def __init__(self):
        pass

    def radix_sort(self, data):
        shift = 1
        for x in range(len(max(data))):
            result = [[] for _ in range(10)]  # [[], [], [], [], [], [], [], [], [], []]
            numbers = [x for x in range(10)]  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            for e, num in enumerate(numbers):
                for arr in data:
                    if num == arr % (shift * 10) // shift:
                        result[e].append(arr)
            data = reduce(lambda x, y: x + y, result)
            shift = shift * 10
        return data
