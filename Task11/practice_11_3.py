def make_calc(op, *args):
    dict_ = {"+": plus, "-": minus, "*": mul}
    return dict_[op](*args)


def plus(*args):
    res_ = args[0]
    for i in args[1:]:
        res_ += i
    return res_


def minus(*args):
    min_ = args[0]
    for i in args[1:]:
        min_ -= i
    return min_


def mul(*args):
    mul_ = args[0]
    for i in args[1:]:
        mul_ = mul_ * i
    return mul_


res = make_calc("+", 1, 5, 1)
print(res)
