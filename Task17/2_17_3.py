# Task 3

class SomethingToDo:

    def __init__(self, arg1):
        self.arg1 = arg1
        self.ind = 0

    def __iter__(self):
        return self

    def __next__(self):
        # for _ in range(len(self.arg1)):
            if self.ind < len(self.arg1):
                res = self.arg1[self.ind]
                self.ind += 1
                return res
            else:
                raise StopIteration

    def __getitem__(self, indx):
        return self.arg1[indx]

    def __repr__(self):
        return f"{self.arg1}"


list_2 = [1, 2, 3, -4, 1, -5, -6, 99, 123, -98, 78]
s = SomethingToDo(list_2)
print(s[3])
for el in s:
    print(s)
