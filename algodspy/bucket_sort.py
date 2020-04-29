class BucketSort:

    def __init__(self):
        self.data = {}

    def bucket_sort(self, alist, reverse=False):
        m = max(alist)
        n = len(alist)
        size = m/n
    
        buckets = [[] for _ in range(n)]
        for i in range(n):
            j = int(alist[i]/size)
            if j != n:
                buckets[j].append(alist[i])
            else:
                buckets[n - 1].append(alist[i])
    

