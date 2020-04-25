class QuickSort:

    def __init__(self):
        pass

    def sort(self, data, reversed=False):
        data_copy = data.copy()
        if len(data_copy) <= 1:
            return data_copy
        else:
            border = data_copy[0]
            left = []
            middle = []
            right = []
            if reversed:
                for x in data_copy:
                    if x > border:
                        left.append(x)
                    elif x == border:
                        middle.append(x)
                    else:
                        right.append(x)
                self.sort(left, True)
                self.sort(right, True)
            else:
                for x in data_copy:
                    if x < border:
                        left.append(x)
                    elif x == border:
                        middle.append(x)
                    else:
                        right.append(x)
                self.sort(left)
                self.sort(right)
            k = 0
            for x in left + middle + right:
                data_copy[k] = x
                k += 1
            return data_copy
