import sys

myinput = sys.argv
myinput = myinput[0:4]


def count_lines(file):
    data = file1.readlines()
    res = len(data)
    return res


def count_chars(file):
    data = file.read()
    data = data.split('\n')
    data3 = ' '.join(data)
    return len(data3[1:-1])


def test_():
    if myinput[1] == 'super':
        res1 = count_lines(file1)
        file1.seek(0, 0)  # возвращаем "каретку" в начало текстового файла
        res2 = count_chars(file1)
        return res1, res2
    elif myinput[1] == '-xc':  # flag for count_lines
        res1 = count_lines(file1)
        return res1
    elif myinput[1] == '-xz':  # flag for count_chars
        res2 = count_chars(file1)
        return res2
    else:
        print("Use correct command -super, -xc, -xz")


with open(myinput[2], 'r', encoding='utf-8') as file1:
    res3 = test_()
    print(f"{res3} in {file1.name}")
