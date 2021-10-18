def sqr_nums(nums):
    li = []
    for num in nums:
        res = num ** 2
        li.append(res)
    print(li)
    return sqr_nums

num1 = [1,2,3,4,5]
sqr_nums(num1)
print(sqr_nums.__code__.co_varnames)
