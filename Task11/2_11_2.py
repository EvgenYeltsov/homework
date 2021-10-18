def sum_nums(x):
    def inner_func(y):
        return x + y
    return inner_func

print(sum_nums(5)(5))
