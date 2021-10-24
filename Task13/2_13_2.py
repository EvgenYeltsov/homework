# Task 2
"""Implement a class Mathematician which is a helper class for doing math operations on lists

The class doesn't take any attributes and only has methods:

    square_nums (takes a list of integers and returns the list of squares)
    remove_positives (takes a list of integers and returns it without positive numbers
    filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'
"""


class Mathematician:
    @staticmethod
    def square_nums(list_of_nums):
        list_res = []
        for el in list_of_nums:
            list_res.append(el ** 2)
        return list_res

    @staticmethod
    def remove_positives(list_of_nums):
        list_res = []
        for el in list_of_nums:
            if el < 0:
                list_res.append(el)
        return list_res

    """Если год не делится на 4, значит он обычный.
    Иначе надо проверить не делится ли год на 100.
    Если не делится, значит это не столетие и можно сделать вывод, что год високосный.
    Если делится на 100, значит это столетие и его следует проверить его делимость на 400.
    Если год делится на 400, то он високосный.
    Иначе год обычный"""
    @staticmethod
    def filter_leaps(list_of_nums):
        list_res = []
        for el in list_of_nums:
            # if el % 4 != 0 or (el % 100 == 0 and el % 400 != 0): Условия для обычного года!
            if el % 4 == 0 or (el % 100 != 0 and el % 400 == 0):
                list_res.append(el)
        return list_res


m = Mathematician()
m.square_nums([7, 11, 5, 4])
m.remove_positives([26, -11, -8, 13, -90])
m.filter_leaps([2001, 1884, 1995, 2003, 2020])

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
