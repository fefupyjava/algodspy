class Fast_Pow():

    def __init__(self, x, n):
        self.x = x
        self.n = n
    
    def __naive(self):
        if self.n < 0:
            self.x  = 1 / self.x
            self.n = -self.n
        if self.n == 0:
            return 1
        y = 1
        while self.n > 1:
            if self.n % 2 == 0:
                self.x = self.x * self.x
                self.n = self.n / 2
            else:
                y = self.x * y
                self.x  = self.x * self.x
                self.n = (self.n - 1) / 2
        return self.x * y
        
    def __recursive(self):
        y = self.x
        if self.n == 0:
            return 1
        elif self.n < 0:
            self.x = 1 / self.x
            self.n *= -1
            return self.__recursive()
        elif self.x == 1:
            return self.x
        elif self.n % 2 == 0:
            self.x *= y
            self.n /= 2
            return self.__recursive()
        elif self.n % 2 == 1:
            self.x *= y
            self.n = (self.n - 1) / 2
            return y * self.__recursive()
    
    def run(self, n, kind):
        if kind == 'naive':
            return self.__naive()
        elif kind == 'recursive':
            return self.__recursive()
        else:
            return('Error')