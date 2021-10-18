"""Реализуйте аккумулирующую функцию.
Примените выражение: (x * y / 21 + x * 42) // y
Используйте reduce, lambda func"""

from _functools import reduce
li = [1, 2, 3, 4]
res = reduce(lambda x, y: (x*y/21 + x*42)//y, li)
print(res)
