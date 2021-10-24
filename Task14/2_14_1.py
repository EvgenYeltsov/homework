# Task 1. Method overloading
from abc import ABC


class Animal:

    def talk(self):
        raise NotImplementedError("Method should be realised")


class Dog(Animal):

    def talk(self):
        return print("woof, woof!")


class Cat(Animal):

    def talk(self):
        return print("meow!")


def talk_again(animal):
    animal.talk()


dog = Dog()
cat = Cat()
dog.talk()
cat.talk()

talk_again(dog)
talk_again(cat)
