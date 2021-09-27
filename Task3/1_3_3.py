# Task1_3_3. Extracting numbers.
import random
i = 0
t = []
while i < 100:
    t.append(random.randint(0, 1000))
    i = i + 1
print(t)
i = 0
t2 = []
while i<len(t):
    if t[i] %7 ==0 and t[i]%5 !=0:
        t2.append(t[i])
    i +=1
print(t2)
