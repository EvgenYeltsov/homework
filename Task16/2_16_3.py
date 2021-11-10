# Task 3
import re


class TypeDecorators:

    @staticmethod
    def convert_to_int(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            if res.isdigit():
                res = int(res)
                return res
            else:
                raise ValueError(" Only numbers")

        return wrapper

    @staticmethod
    def convert_to_str(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            for el in res:
                if isinstance(el, int):
                    raise ValueError('No integers inside list')
                else:
                    res = ''.join(res)
            return res

        return wrapper

    @staticmethod
    def convert_to_bool(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            if res == 'True':
                res = True
            if res == 'False':
                res = False
                return res
            else:
                raise ValueError(" Only string <False> or <True>")

        return wrapper

    @staticmethod
    def convert_to_float(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            regex = "^[0-9]+[.]?[0-9]$"
            if re.match(regex, res):
                res = float(res)
                return res
            else:
                raise ValueError(" Only numbers")

        return wrapper


@TypeDecorators.convert_to_int
def do_nothing(string: str):
    return string


do_nothing('6677')
assert do_nothing('6677') == 6677, 'Something is wrong'


@TypeDecorators.convert_to_str
def do_nothing_with_list(list_: list):
    return list_


do_nothing_with_list(['4', '434', 'ffder'])
assert do_nothing_with_list(['4', '434', 'ffder']) == '4434ffder'


@TypeDecorators.convert_to_bool
def do_nothing_bool(string: str):
    return string


do_nothing_bool('False')
assert do_nothing_bool('False') == False


@TypeDecorators.convert_to_float
def do_nothing_float(string: str):
    return string


do_nothing_float('45')
assert do_nothing_float('45') == 45.0
