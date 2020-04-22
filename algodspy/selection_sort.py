class SelectionSort:

    def __init__(self):
        pass

    def sort(self, array, reverse=False):
        n = len(array)
        for i in range(n):
            m = i
            for j in range(i, n):
                if array[j] < array[m]:
                    m = j
            array[i], array[m] = array[m], array[i]
        if reverse:
            return array[::-1]
        else:
            return array
