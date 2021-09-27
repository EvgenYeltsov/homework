# Task1_3_1. Greatest numbers of list.
import random

i = 0
t = []
while i < 10:
    t.append(random.randint(0, 99))
    i = i + 1
print("Строка для определения максимума", t)
print("Максимум", max(t))
