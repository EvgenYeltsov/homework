# Task1_3_2.Exclusive common numbers.
import random
i = 0
t = []
t1 = []
while i < 10:
    t.append(random.randint(0, 5))
    t1.append(random.randint(0, 5))
    i = i + 1
print(t, '\n', t1,)
t2 = t + t1
t2 = sorted(t2)
i = 0
t3 = []
while i < len(t2):
    if t2[i] != t2[i-1]:
        t3.append(t2[i])
    i = i +1
print("New list without duplicates", t3)
