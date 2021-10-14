# Task 1_8_3. A simple calculator.
def make_operation(operator, *args):
    argument = args[0]
    for i in range(len(args)-1):
        argument = f" {argument}{operator}{args[i+1]}"
        res_1 = eval(argument)
    return print(res_1, argument)


make_operation('+', 7, 7, 8)
make_operation('-', 5, 5, -10, -20)
make_operation('*', 7, 6)
