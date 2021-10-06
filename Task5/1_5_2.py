# Task 1_5_2. The valid phone number program.
line_1 = input("Please write your phone number 10 symbols:")
if line_1.isdigit() and len(line_1) == 10:
    print("Correct number, follow next tips")
else:
    print("Error wrong phone number")
