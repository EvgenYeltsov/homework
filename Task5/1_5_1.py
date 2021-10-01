# Task 1_5_1. String manipulation
line_1 = input("Введите текстовую строку:")
# Предполагаем, что все символы строки являются буквами или цифрами
if not line_1.isalnum():
    print("Введены не корректные символы")
    exit(1)
if len(line_1) < 2:
    print("Пустая строка")
else:
    slice_1 = line_1[:2] + line_1[-2:]
    print("Результат", slice_1)
