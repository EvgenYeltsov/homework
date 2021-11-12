#Task 2_20_1

from datetime import datetime
import os


class CM:

    def __init__(self, file_name):
        self.count = 0
        self.file_name = file_name
        self.file = None

    def __enter__(self):
        self.file = open(self.file_name)
        self.start = str(datetime.now())
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Подсчет сколько раз был открыт файл (метод так себе)!!!!
        # with open('login.txt', 'r') as file1:
        #     data = file1.readlines()
        #     res = len(data)
        with open('login.txt', 'a') as file1:
            file1.write(f"user open {self.file.name} > {res} < times at {self.start[:19]}\n")
        return None


with CM('something_inside.txt') as cm:
        cm.read()

