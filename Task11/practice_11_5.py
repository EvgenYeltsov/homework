li = ['a', 'ab', 'abc', 'abed']
res2 = list(map(lambda x: (x, len(x)), li))
print(res2, type(res2))


