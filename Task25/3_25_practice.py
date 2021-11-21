# Task 2

class RecursiveUtils():

    # Перевод строки из чисел в список чисел "132" -> [1, 2, 3]

    def str_to_int(self, str_input, list_=[]):

        if len(str_input) == 1:
            list_.append(int(str_input))
            return list_

        list_.append(int(str_input[0]))
        self.str_to_int(str_input[1:])
        return list_

    # Посчитайте факториал 5! -> 120

    def calc_fact(self, n: int) -> int:
        if n <= 1:
            return n
        return n * self.calc_fact((n - 1))

    # Посчитайте нули в поданной числовой строке: "010203" -> 3

    def calc_zero(self, input_str, list2=[]):
        if len(input_str) == 1:
            return input_str[0]
        if input_str[0] == '0':
            list2.append(input_str[0])
        self.calc_zero(input_str[1:])
        return len(list2)

    # Посчитайте нули в поданном числе: 102 -> 1

ex1 = RecursiveUtils()
print(ex1.str_to_int('123456'))
ex2 = RecursiveUtils()
print(ex2.calc_fact(5))
ex3 = RecursiveUtils()
print(ex1.calc_zero('123040506'))
