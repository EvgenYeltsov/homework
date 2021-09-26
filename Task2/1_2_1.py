# Task 1_2_1. The greeting program.
# Using f-string.
name = 'yevgeny'
day = 'sunday'
print(f"\"Good day {name.title()}! {day.upper()} is a perfect day to learn some python.\"\n")
# Using %-format.
print("\"Good day %(name)s ! %(day)s is a perfect day to learn some python.\"" % {"name": name.title(), "day": day.upper()})
