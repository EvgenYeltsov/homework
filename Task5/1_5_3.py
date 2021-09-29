# Task 1_5_3. The name check.
my_name = 'evgeny'
str_1 = input("Please write your name:")
if str_1 == my_name or str_1 == my_name.title():
   print("Welcome", str_1)
else:
   print("Access denied")
