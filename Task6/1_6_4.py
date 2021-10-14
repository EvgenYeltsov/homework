# Task 1_6_4. Lesson 6. Additional Task 1
import sys

parameters = sys.argv
h_piram = parameters[1]
h_piram = int(h_piram)

j = h_piram-1
for i in range(h_piram*2):
    if i > h_piram:
        print("x"*j)
        j -= 1
    else:
        print("x"*i)
