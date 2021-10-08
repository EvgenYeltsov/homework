# Task 1_8_2.Creating a dictionary.
dict_country = {}


def make_country(country_name, capitals):
    dict_country.update({country_name: capitals})


make_country('Ukraine', 'Kiev')
make_country('England', 'London')
make_country('Kazahstan', 'Nursultan')

print(dict_country)
