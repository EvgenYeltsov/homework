"""Напишите функцию, которая принимает на вход три аргумента:
 1 - название страны,
 2 - название моря или океана, омывающих берега этой страны,
 3 - словарь, который необходимо обновить новыми данными.

Структура словаря: seas_oceans = {country: [ocean, sea1, sea2..]}

Вызовите несколько раз созданную функцию, заполните словарь данными
Создайте .json файл, используя фукнцию open() в контекстном менеджере, режим - 'a'
С помощью библиотеки json сохраните словарь в указанный файл. Используйте метод json.dump(fd)
Откройте заново файл через open()
С помощью библиотеки json считайте данные из файла, конвертируя их из строки обратно в словарь.
Выведите словарь на экран. Используйте метод json.load(fd)"""
import json


def country_info(country, sea, sea_oceans_):
    return sea_oceans_.update({country: sea})


sea_oceans = {}
country_info('Ukraine', ['Azov sea', 'Black sea'], sea_oceans)
country_info('USA', ['Atlantic ocean', 'Pacific ocean'], sea_oceans)

# print(sea_oceans)

with open("country_info.json", "w") as data:
    json.dump(sea_oceans, data, indent=2)

with open("country_info.json") as data:
    info_in = json.load(data)
    print(info_in)
