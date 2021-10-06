import sys


params = sys.argv
if len(params) != 2:
    print("input only one string [12asddfDDF]")
    exit(1)

str_input = params[1]
str_input = str_input.lower()
i = 0
res_tab = []
while i < len(str_input):
    z_count = str_input.count(str_input[i])
    res_tab = [(str_input[i], z_count)] + res_tab
    i += 1
res_tab = set(res_tab)
res_tab = list(res_tab)
print(res_tab)
