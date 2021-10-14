def string_line(string_line_1):
    new_string_line = string_line_1.split()
    new_string_line1 = ' '.join(new_string_line)
    if new_string_line1[-1] == '.':
        print(new_string_line1.lower())
    else:
        print(new_string_line1.lower(), end='.')


string_line("   hEllo     world     rtg.  ")
