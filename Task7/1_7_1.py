# Task 1_7_1. The Guessing Game.
import random

u_name = input("Welcome, guest. You have 10 lives for win. Your name: ")
if not u_name.isalpha():
    print("Please input valid name")
    exit(1)

i = 0
count_win = 0
count_pc = 0
while i <= 10:
    u_num = input("Input number in range 1-10 maybe you guess:=")
    if not u_num.isdigit():
        print("only numbers")
        exit(1)
    u_num = int(u_num)
    c_num = random.randint(1, 10)
    if u_num == c_num:
        count_win = count_win + 1
        print(f"\"Great {u_name.title()} you are lucky, you win = {count_win} time. {u_num} '=' {c_num}")
    else:
        count_pc = count_pc + 1
        print(f"\"Try again {u_num} not equal {c_num}  Computer win! {count_pc} times")
    i += 1
