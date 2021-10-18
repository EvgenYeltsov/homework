# Task 1_10_1.
# def oops():
#     raise IndexError
#
#
# def another_function():
#     try:
#         oops()
#     except IndexError:
#         return print("no Error")
#
#
# another_function()

# raise KeyError

def oops_1():
    raise KeyError


def another_function_1():
    try:
        oops_1()
    except IndexError:
        return print("no Error")


another_function_1()
