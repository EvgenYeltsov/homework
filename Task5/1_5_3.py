# Task 1_5_3. The name check.
# my_name = 'evgeny'
# str_1 = input("Please write your name:")
# if str_1 == my_name or str_1 == my_name.title():
#    print("Welcome", str_1)
# else:
#    print("Access denied")

# с использованием функции lower. Дает вводить любые символы имени в любом регистре и получать на выходе True
my_name = 'evgeny'
str_1 = input("Please write your name:")
str_1 = str_1.lower()
if str_1 == my_name:
    print("Welcome", str_1)
else:
    print("Access denied")
