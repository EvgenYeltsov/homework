# Task 4

"""def reverse(input_str: str) -> str:
 Function returns reversed input string
 reverse("hello") == "olleh"
    True
 reverse("o") == "o"
    True
"""


def reverse(input_str: str) -> str:
    if len(input_str) <= 1:
        return input_str[-1]
    res = input_str[-1] + reverse(input_str[:-1])
    return res


print(reverse('hello'))
print(reverse('o'))
