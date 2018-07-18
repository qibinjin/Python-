class fibonacci(object):
    def __init__(self, num):
        self.num = num
        self.a = 0
        self.b = 1
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current <= self.num:
            ret = self.a
            self.a, self.b = self.b, self.a + self.b
            return ret
        else:
            raise StopIteration


if __name__ == '__main__':
    fib = fibonacci(5)
    a = []
    a.extend(fib)
    print(a)
