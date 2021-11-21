# Task 3

"""def mult(a: int, n: int) -> int:
    This function works only with positive integers
mult(2, 4) == 8
    True
mult(2, 0) == 0
    True
 mult(2, -4)
ValueError("This function works only with postive integers")

    2*5 = 5+5
    3*6 = 6+6+6
"""


def mult(a: int, n: int) -> int:
    if n < 0:
        raise ValueError("This function works only with postive integers")
    elif a <= 0:
        return a
    return n + mult(a - 1, n)


assert mult(3, 4) == 12
assert mult(2, 0) == 0
# assert mult(2, -4)
