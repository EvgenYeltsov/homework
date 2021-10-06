import sys


params = sys.argv
if len(params) != 2:
    print("input only one string [122334]")
    exit(1)

x = params[1]

if not x.isdigit:
    print("input only numbers 1234567890")
    exit(1)

i = 0
sum_1 = 0
while i < len(params[1]):
    sum_1 = int(x[i])+sum_1
    i += 1
print(sum_1)
