class QuickSort:

    def __init__(self):
        pass

    def sort(self, data, reversed=False):
        data = data.copy()
        if len(data) <= 1:
            return data
        else:
            border = data[0]
            left = []
            middle = []
            right = []
            if reversed:
                for x in data:
                    if x > border:
                        left.append(x)
                    elif x == border:
                        middle.append(x)
                    else:
                        right.append(x)
                left = self.sort(left, True)
                right = self.sort(right, True)
            else:
                for x in data:
                    if x < border:
                        left.append(x)
                    elif x == border:
                        middle.append(x)
                    else:
                        right.append(x)
                left = self.sort(left)
                right = self.sort(right)
            k = 0
            for x in left + middle + right:
                data[k] = x
                k += 1
            return data
