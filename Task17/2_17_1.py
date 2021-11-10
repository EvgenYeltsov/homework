# Task 1.

def new_enumerate(iterable, start=0):
    if type(iterable) == int:
        for n in range(iterable):
            start += 1
            yield f" #{start} - {n}"
    else:
        for n in iterable:
            start += 1
            yield f" #{start} - {n}"


""" only int, str, list, tuple"""

a = new_enumerate(5)
print(type(a))

for i in a:
    print(i)

