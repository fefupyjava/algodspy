class QuickSort:

    def __init__(self):
        pass

    def sort(self, data, reversed=False):
        if len(data) <= 1:
            return data
        else:
            border = data[0]
            l = []
            m = []
            r = []
            if reversed:
                for x in data:
                    if x > border:
                        l.append(x)
                    elif x == border:
                        m.append(x)
                    else:
                        r.append(x)
                self.sort(l, True)
                self.sort(r, True)
            else:
                for x in data:
                    if x < border:
                        l.append(x)
                    elif x == border:
                        m.append(x)
                    else:
                        r.append(x)
                self.sort(l)
                self.sort(r)
            k = 0
            for x in l + m + r:
                data[k] = x
                k += 1
            return data
