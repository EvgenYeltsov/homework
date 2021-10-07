# Task 1_7_4. Math quiz program.
import random


print("You are welcome to a Big Math QUIZ")
count_u = 0
while True:
    math_l = ['+', '-', '*']
    math_l_r = random.choice(math_l)
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c_sum = a + b
    c_dif = a - b
    c_pro = a*b
    user = input(f"Введите ответ {a} {math_l_r} {b} := ")
# Есть баг. Если выпадает 1 и любое другое число а знак + или -. Пример 1 - 4 = -3
# но если ввести 4 ты тоже выиграл
    if user == 'q':
        print("Good bay friend")
        exit(0)
    elif int(user) == c_sum or int(user) == c_dif or int(user) == c_pro:
        count_u = count_u + 1
        print(f"Win {count_u} time")
    else:
        print("Try again")
        count_u = 0
    continue
