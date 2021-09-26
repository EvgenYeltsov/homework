# Task 1_2_3. Calculator.
print("Добрый день")
a = input("Введите число а = ")
b = input("Введите число b = ")
a = float(a)
b = float(b)
print("a =", a, '\t', "b = ", b)
operation_list = [" ", "1.Складывание", "2.Вычитание", "3.Деление",
                  "4.Умножение", "5.Возведение числа \"а\" в степень \"b\"",
                  "6.Модуль для числа \"а\"", "7.Деление с округлением"]
print("Сделайте Ваш выбор, введите целое число от 1 до 7 ", str(operation_list[1:8]).replace(',', '\n'), sep='\n')
x = input("Ваш выбор =")
x = int(x)
print(operation_list[x])
addition = a + b
subtraction = a - b
division = a/b
multiplication = a*b
exponent = a**b
modulus = abs(a)
floor_d = a // b
operation_list_run = [0, float(addition), float(subtraction), float(division),
                      float(multiplication), float(exponent), float(modulus),
                      float(floor_d)]
print("Результат = ", operation_list_run[x])
# Для проверки всех математических действий сразу
# s = str(operation_list_run)
# print("Результат =", s.replace(',', '\n'))
