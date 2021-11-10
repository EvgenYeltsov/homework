class Filter:

    def __init__(self, func, li_):
        self.func = func
        self.li_ = li_
        self.ind = 0

    def __iter__(self):
        return self

    def __next__(self):
        for _ in range(len(self.li_)):
            if self.func(self.li_[self.ind]) and self.ind < len(self.li_):
                res = self.li_[self.ind]
                self.ind += 1
                return res
            elif not self.func(self.li_[self.ind]):
                self.ind += 1
                res = None
                del res
            else:
                raise StopIteration

    """полуить срез и значение по ключю"""
    def __getitem__(self, key):
        if isinstance(key, int) and key < len(self.li_):
            return self.li_[key]
        elif isinstance(key, slice):
            return self.li_[key.start:key.stop:key.step]
        else:
            raise IndexError


li = [1, 2, 3, -4, 1, -5, -6, 99, 123, -98, 78]
filter_ = Filter(lambda x: x > 0, li)
# List out of range. Fix later.
try:
    for el in filter_:
        print(el)
except IndexError:
        print("need to Fix")

print(filter_[1:4:2])
print(filter_[6])