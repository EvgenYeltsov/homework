def new_user(user_n):
    list_1 = ['name', 'surname']
    list_2 = []
    user_n = int(user_n)
    for user_n in range(len(list_1)):
        user_data_1 = input(f"please insert your {list_1[user_n]}")
        list_2.append(user_data_1)
    print(list_2)

new_user(3)
