# Task 1_10_2.
def squared(a_1, b_1):
    return int(a_1) ** 2 / int(b_1)


try:
    a = input("a =")
    b = input("b =")
    # if not a.isdigit() and b.isdigit() or b == '0':
    #     raise ValueError
    print(squared(a, b))
except (ValueError, ZeroDivisionError):
    print("only numbers")
