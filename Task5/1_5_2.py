# Task 1_5_2. The valid phone number program.
str_1 = input("Please write your phone number:")
if str_1.isdigit() and len(str_1) == 10:
   print("Corect number")
else:
   print("Error wrong phone number")