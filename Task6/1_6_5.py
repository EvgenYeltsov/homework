# Task 1_6_5. Lesson 6. Additional Task 2
import sys

if len(sys.argv) != 2:
    print("input valid data")
    exit(1)

foo1 = sys.argv[1]
foo1 = foo1.lower()
dict_foo = {}
for i in foo1:
    if i in dict_foo:
        dict_foo[i] += 1
    else:
        dict_foo[i] = 1
print(dict_foo)
