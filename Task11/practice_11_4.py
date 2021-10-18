# 1 - Через dict
# def make_calc(oper):
#     def plus(*args):
#         res_ = args[0]
#         for i in args[1:]:
#             res_ += i
#         return res_
#
#     def minus(*args):
#         min_ = args[0]
#         for i in args[1:]:
#             min_ -= i
#         return min_
#
#     def mul(*args):
#         mul_ = args[0]
#         for i in args[1:]:
#             mul_ = mul_ * i
#         return mul_
#
#     dict_ = {"+": plus, "-": minus, "*": mul}
#     return dict_[oper]
#
#
# res = make_calc("-")(4, 7)
# print(res)

# 2- Через if блок
def make_calc(func):
    if func == "+":
        def plus(*args):
            plus_ = args[0]
            for i in args[1:]:
                plus_ += i
            return plus_

        return plus

    elif func == "-":
        def minus(*args):
            min_ = args[0]
            for i in args[1:]:
                min_ -= i
            return min_

        return minus
    elif func == "*":
        def mul(*args):
            mul_ = args[0]
            for i in args[1:]:
                mul_ = mul_ * i
            return mul_

        return mul


res = make_calc("-")(4, 7)
print(res)
