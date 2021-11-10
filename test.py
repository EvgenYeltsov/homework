import sys

# myinput = sys.argv
# myinput = myinput[0:4]
#
#
# def count_lines(*args):
#         with open(myinput[2], 'r', encoding='utf-8') as file:
#             data = file.readlines()
#             res = len(data)
#         return res
#
#
# def count_chars(*args):
#         with open(myinput[2], 'r', encoding='utf-8') as file:
#             data = file.read()
#             data = data.split('\n')
#             data2 = ' '.join(data)
#             return len(data2[1:-1])
#
#
# if myinput[1] == 'super':
#     def test_(*args, **kwargs):
#         return print(count_lines('xc') , count_chars('xz'))
#     run_ = test_(myinput[2])
#
# elif myinput[1] == 'xc':
#     def test_(*args, **kwargs):
#         return print(count_lines())
#     run_ = test_(myinput[2])
#
# elif myinput[1] == 'xz':
#     def test_(*args, **kwargs):
#         return print(count_chars())
#     run_ = test_(myinput[2])
#
# else:
#     print("print correct command, xc - count_lines, xz - count_chars")

# Version 2.

myfile = 'some_txt.txt'


def count_lines(*args):
    with open(myfile, 'r', encoding='utf-8') as file:
        data = file.readlines()
        res = len(data)
    return res


def count_chars(*args):
    with open(myfile, 'r', encoding='utf-8') as file:
        data = file.read()
        data = data.split('\n')
        data2 = ' '.join(data)
        return len(data2[1:-1])


def test_(*args, **kwargs):
    return count_lines(), count_chars()


def rewind(f):
    f.seek(0, 0)


run_ = test_()
print(run_)

