# Task 3

class FiboNums:

    def __init__(self, num):
        self.num = num
        self.ind = 0
        self.start1 = 0
        self.start2 = 1


    def __iter__(self):
        return self

    def __next__(self):
        if self.ind <= self.num:
            res = self.start1 +self.start2
            self.start1 = self.start2
            self.start2 = res
            self.ind += 1
            return res
        raise StopIteration

fib = FiboNums(11)
for el in fib:
    print(el)
