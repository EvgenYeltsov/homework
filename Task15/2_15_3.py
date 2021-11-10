# Task 3

""""Write a decorator `arg_rules` that validates arguments passed to the function.
A decorator should take 3 arguments:
max_length: 15
type_: str
contains: [] - list of symbols that an argument should contain
If some of the rules' checks returns False, the function should return False and print the reason it failed;
 otherwise, return the result."""

from functools import wraps


def arg_rules(type_, lenght, contains):
    def inner_wrapper(func):
        @wraps(func)
        def wrapper(name):
            res = func(name)
            if len(name) > lenght:
                return False
            if type(name) != type_:
                return False
            for el in contains:
                if el not in name:
                    return False
            return res
        return wrapper
    return inner_wrapper


@arg_rules(type_=str, lenght=15, contains=['05', '@'])
def create_slogan(name):
    return f"{name} drinks pepsi in his brand new BMW!"


sl1 = create_slogan('RTSA0hu0505#@')
sl2 = create_slogan('jhondoiddddl@gmail.com')
# print(sl1)
# print(sl2)

assert sl2 is False

assert create_slogan('RTSA0hu0505#@') == 'RTSA0hu0505#@ drinks pepsi in his brand new BMW!', 'Something wrong'
