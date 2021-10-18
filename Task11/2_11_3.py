def sqr_nums(nums):
    li = []
    for num in nums:
        res = num ** 2
        li.append(res)
    print(li)
    return sqr_nums


def remove_negatives(nums):
    li = []
    for num in nums:
        if num > 0:
            li.append(num)
    print(li)
    return remove_negatives


def choose_func(nums, func1, func2):
    if all(el > 0 for el in nums):
        return func1(nums)
    else:
        return func2(nums)


nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]
x = choose_func(nums2, sqr_nums, remove_negatives)
print(x)
