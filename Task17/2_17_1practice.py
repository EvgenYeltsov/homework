def custom_filter(func, iter):
    for el in iter:
        if func(el):
            yield el


li = [1, 2, 3, -4, -5, 8]
print(list(custom_filter((lambda x: x > 0), li)))
