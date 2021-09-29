# Task 1_5_1. String manipulation
str_1 = input("Введите строку:")
if len(str_1) < 2:
   print("Empty String")
else:
   slice_1 = str_1[:2] + str_1[-2:]
   print("Результат", slice_1)
