# Task 1_6_7. Lesson 6. Additional Task 4
import sys

snt = sys.argv[1:]
# перевод в нижний регистр
for i in range(len(snt)):
    snt[i] = snt[i].lower()
# новый словарь
res_dict = {}
for i in snt:
    if i in res_dict:
        res_dict[i] += 1
    else:
        res_dict[i] = 1
print(res_dict)
