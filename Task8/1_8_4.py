import sys

num = sys.argv[1]
exp_1 = sys.argv[2]

def ex_res(num, exp_1):
    res = int(num)**int(exp_1)
    return res

res_fun = ex_res(num, exp_1)
print(f"{num}**{exp_1} = {res_fun}")
