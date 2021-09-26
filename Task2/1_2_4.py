# Task 1_2_4. Additional task.
# f-string
you = 'Yevgeny'
weather = 'cold'
print(f"Hey,{you} is it {weather} today ?")
# % format
you = 'Yevgeny'
weather = 'cold'
print("Hey, %(you)s is it %(weather)s today ?" % {"you": you, "weather": weather})
# concatenation
you = 'Yevgeny'
weather = 'cold'
print("Hey" + ' ' + you + ' ' + "is it" + ' ' + weather + ' ' + "today ?")
# format
you = 'Yevgeny'
weather = 'cold'
print("Hey,{} is it {} today ?". format(you, weather))
