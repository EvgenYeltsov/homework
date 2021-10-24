# Task 1.
"""Make a class structure in python representing people at school.
Make a base class called Person, a class called Student, and another one called Teacher.
Try to find as many methods and attributes as you can which belong to different classes,
and keep in mind which are common and which are not.
For example, the name should be a Person attribute, while salary should only be available to the teacher."""


class Person:
    def __init__(self, name, blood_type, age):
        self.name = name
        self.blood_type = blood_type
        self.age = age


class Teacher(Person):
    def __init__(self, salary, name, blood_type, age):
        super().__init__(name, blood_type, age)
        self.salary = salary

    def add_salary(self):
        self.salary = self.salary + 1


class Student(Person):
    def __init__(self, grant, name, blood_type, age):
        super().__init__(name, blood_type, age)
        self.grant = grant

    def add_grant(self):
        self.grant = self.grant + 100


person_1 = Student(100, "Makr", "A(II)+", 20)
person_2 = Teacher(1000, "Luka", "AB(IV)-", 20)
person_1.add_grant()
print(person_1.grant)
print(person_1.name)
person_2.add_salary()
print(person_2.salary)
