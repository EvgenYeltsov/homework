def make_calc(op, *args):
    dict_ = {"+": plus, "-": minus, "*": exp}
    return dict_[op](*args)


def plus(*args):
    res = args[0]
    for i in args[1:]:
        res += i
    return res


def minus(*args):
    min_ = args[0]
    for i in args[1:]:
        min_ -= i
    return min_


def exp(*args):
    exp_ = args[0]
    for i in args[1:]:
        exp_ = exp_ * i
    return exp_


res = make_calc("+", 1, 2, 1)
print(res)
