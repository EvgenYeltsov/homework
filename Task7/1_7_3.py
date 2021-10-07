# Task 1_7_3. Words combination.
import random


k_word = input("Input something in string format = ")
k_word = list(k_word)
for i in range(5):
    k_new = random.sample(k_word, len(k_word))
    k_new_s = ''.join(k_new)
    print(k_new_s, type(k_new_s))
