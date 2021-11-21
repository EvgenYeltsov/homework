#Task2

"""def is_palindrome(looking_str: str, index: int = 0) -> bool:
Checks if input string is Palindrome
('mom')
True
('sassas')
True
is_palindrome('o')
True
"""


from typing import List, Set, Dict, Tuple, Optional, Iterable

def is_palindrome(looking_str: str, index: int = 0) -> bool:
    if len(looking_str) <= 1:
        return True
    else:
        return looking_str[0] == looking_str[-1] and is_palindrome(looking_str[1:-1])

print(is_palindrome('mom'))
print(is_palindrome('momy'))
print(is_palindrome('m'))






