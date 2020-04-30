class BinarySearch:
    def __init__(self):
        pass
        
    def __naive(self, data, x):
        if len(data) == 0:
            return -1
        mid = len(data) // 2
        first = 0
        last = len(data) - 1
    
        while data[mid] != x and first <= last:
            if x > data[mid]:
                first = mid + 1
            else:
                last = mid - 1
            mid = (first + last) // 2
    
            if first > last:
                return -1
            else:
                return mid

    def __recursive(self, data, x):
        if len(data) == 0:
            return -1
        else:
            mid = len(data) // 2
            if data[mid] == x:
                return mid
            else:
                if x < data[mid]:
                    return self.__recursive(data[:mid], x)
                else:
                    return self.__recursive(data[mid+1:], x)
    
    def run(self, data, x, kind='naive'):
        if kind == 'naive':
            return self.__naive(data, x)
        if kind == 'recursive':
            return self.__recursive(data, x)