# Task2. Library.
class Library:
    all_book = []

    def __init__(self, name):
        self.name = name
        self.list_book = []
        self.list_author = []

    def new_book(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        self.list_book.append([name, year, author])
        self.list_author.append(author)
        Library.all_book.append(name)
        # return print(self.list_book, '\n', self.list_author)
        repr(self.list_author)

    def group_by_author(self, author):
        self.author = author
        autor_list = []
        for auth in self.list_book:  # проверяем список
            for auth2 in auth:       # проверяем вложенный список
                if author in auth:
                    autor_list.append(auth2)
        print(autor_list)
        return

    def group_by_year(self, year):
        self.year = year
        year_list = []
        for auth in self.list_book:
            for auth2 in auth:
                if year in auth:
                    year_list.append(auth2)
        print(year_list)


class Book:

    def __init__(self):
        count = 0
        for book in range(len(Library.all_book)):
            count += book
        print(count)


class Author:

    def __init__(self, name, country, birthday, book):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.book = book
        Library.all_book.append(book)


l = Library('Prog')
l1 = Library('Fan')
a1 = Author('Mark', 'USA', 1970, ['Python 5th', 'Python 3th'])
l.new_book('Learning Python  5th ', 2019, a1.name)
a2 = Author('FunFun', 'USA', 1970, ['Comedy', 'Vi'])
l.new_book('comedy ', 2020, a2.name)

l.group_by_author('FunFun')
# print(Library.all_book)
l.group_by_year(2019)
