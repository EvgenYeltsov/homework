# Task 1_6_8. Lesson 6. Additional Task 5
import sys
import random

qty = sys.argv[1]

# if sys.argv[1] == ' ':
#     print("ok generate 10 numbers")

i = 1
l1 = []
for i in range(int(qty)):
    while i <= 10:
        d = random.randint(0, 9)
        l1.append(d)
        i += 1
    print("+380", "(", l1[1], l1[2], l1[3], ")")

