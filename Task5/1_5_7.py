H_piramida = input(" Введите высоту пирамиды: ")
if not H_piramida.isdigit():
    print("Введены некорректные символы")
    exit(1)
H_piramida = int(H_piramida)
i = 1
while i <= H_piramida:
    print("+"*i)
    i += 1
i = H_piramida - 1
while i > 0:
    print("+"*i)
    i -= 1

