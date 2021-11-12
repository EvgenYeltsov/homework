# Task2


def in_range(start, stop, step=1):
    if step is None:
        while start < stop:
            yield start
            start += 1
    else:
        while start < stop:
            yield start
            start += step


a = in_range(1, 5, 1)
print(type(a))
for el in a:
    print(el)
