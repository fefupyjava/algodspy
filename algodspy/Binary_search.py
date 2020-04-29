class BinarySearch:
    def __init__(self, data, x):
        self.data = data
        self.x = x
        
    def run(self, kind='naive'):
        if kind == 'naive':
            if len(self.data) == 0:
                return -1
            mid = len(self.data) // 2
            first = 0
            last = len(self.data) - 1
    
            while self.data[mid] != self.x and first <= last:
                if self.x > self.data[mid]:
                    first = mid + 1
                else:
                    last = mid - 1
                mid = (first + last) // 2
    
                if first > last:
                    return -1
                else:
                    return mid
        if kind == 'recursive':
            if len(self.data) == 0:
                return -1
            else:
                mid = len(self.data) // 2
                if self.data[mid] == self.x:
                    return mid
                else:
                    if self.x < self.data[mid]:
                        return BinarySearch.run(self.data[:mid],self.x)
                    else:
                        return BinarySearch.run(self.data[mid+1:],self.x)