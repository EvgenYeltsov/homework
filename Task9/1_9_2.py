# Task9. 1_9_2. Phone search
import json

choice_list = "1-add new user  2 - search user 3 - delete by phone number 4 - update info by phone 5 - all list Q -exit"
print("Welcome to phonebook, please make your choice")


def user_add():
    user_list = ['name', 'surname', 'city']
    user_dict = {'name': '', 'surname': '', 'city': ''}
    while True:
        user_key = input("phone number")
        if not user_key.isdigit():
            print("Only numbers")
            exit(1)
        break
    for key in user_list:
        user_info_input = input(f"Please write your {key} - ").lower()
        user_dict[key] = user_info_input
    user_dict_f = {user_key: user_dict}  # вложенный словарь
    # Почему-то если файл обновлять (a- update) он создает словари для каждого пользователя,
    # но не создает один главный словарь!?
    # with open("data.json", "a") as f:
    #     json.dump(user_dict_f, f, indent=4)
    with open("data.json", "r") as file:
        data_file = json.load(file)
    data_file.update(user_dict_f)
    with open("data.json", "w") as file:
        json.dump(data_file, file, indent=4)
    return print("user add")


def search_user():
    user_input = input("search by - ").lower()
    with open("data.json") as file_data:
        phonebook_data = json.load(file_data)
        for key in phonebook_data.keys():
            if user_input == key:
                print(user_input, phonebook_data.get(user_input))
                break
            for value in phonebook_data[key].items():
                if user_input in value:
                    print(key, phonebook_data[key])
                break


def user_del():
    user_input = input("delete number - ").lower()
    with open("data.json") as file_data:
        phonebook_data = json.load(file_data)
        for key in phonebook_data.keys():
            if user_input == key:
                print(f"user with phone number {key} deleted")
                phonebook_data.pop(key)
                break
    with open("data.json", "w") as file_data:
        json.dump(phonebook_data, file_data, indent=4)


def print_all_users():
    with open("data.json") as file_data:
        phonebook_data = json.load(file_data)
        for key in phonebook_data.keys():
            print("phone number", key, phonebook_data[key])


def update_user_info():
    user_input = input("update user info with number - ").lower()
    with open("data.json") as file_data:
        phonebook_data = json.load(file_data)
        for key in phonebook_data.keys():
            if user_input == key:
                for _ in phonebook_data[key].items():
                    user_input_a_n = input("update name").lower()
                    user_input_a_s = input("update surname").lower()
                    user_input_a_c = input("update city").lower()
                    new_dict = {'name': user_input_a_n, 'surname': user_input_a_s, 'city': user_input_a_c}
                    phonebook_data[key] = new_dict
                    print(phonebook_data[key].values())
                    break
    with open("data.json", "w") as file_data:
        json.dump(phonebook_data, file_data, indent=4)


while True:
    user_choice = input(f"{choice_list} \n:=")
    if user_choice == '1':
        user_add()
    elif user_choice == '2':
        search_user()
    elif user_choice == '3':
        user_del()
    elif user_choice == '4':
        update_user_info()
    elif user_choice == '5':
        print_all_users()
    elif user_choice == 'Q':
        print("Bye")
        exit(0)
    else:
        print("input correct data")
        exit(1)
    continue
