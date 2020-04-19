class BubbleSort:
    def __init__(self):
        pass

    def sort_buff(self,data):
        for i in range(len(data) - 1):
            for j in range(len(data) - i - 1):
                if data[j] > data[j + 1]:
                    buff = data[j]
                    data[j] = data[j + 1]
                    data[j + 1] = buff
        return data
    
    def sort_nerf(self,data):
        for i in range(len(data) - 1):
            for j in range(len(data) - i - 1):
                if data[j] < data[j + 1]:
                    nerf = data[j]
                    data[j] = data[j + 1]
                    data[j + 1] = nerf
        return data