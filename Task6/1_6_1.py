# Task 1_6_1
input_string = input("Please input something in string format: ")
if input_string.isdigit():
    print("Please string format only")
    exit(1)

res_dict = {}
input_string = input_string.split()
for i in input_string:
    count_1 = input_string.count(i)
    res_dict.update({i: count_1})
print(res_dict)
