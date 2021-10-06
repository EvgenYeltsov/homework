import sys


params = sys.argv
if len(params) != 2:
    print("input only one string in format"" \"YOUR TEXT HERE\"""")
    exit(1)

x = list(params[1:])
x = ' '.join(x)
x = x.split()
x.reverse()
y = ' '.join(x)
print("\"", y, "\"",  type(y))
