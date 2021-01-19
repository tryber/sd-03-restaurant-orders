# import csv


def best_seller_by_client(client, dict):
    count = {}
    client_list = dict[client]
    client_dish_and_day = client_list[0]
    most_frequent = client_dish_and_day[0]

    for dish, day in client_list:
        if dish not in count:
            count[dish] = 1
        else:
            count[dish] += 1
        if count[dish] > count[most_frequent]:
            most_frequent = dish
    return most_frequent


def favorite_dish_by_client(client, selected_dish, dict):
    count = {}
    client_list = dict[client]
    for dish, day in client_list:
        if dish not in count:
            count[dish] = 1
        else:
            count[dish] += 1

    return count[selected_dish]


def get_total_dish(dict):
    dishes = set()
    for client, orders in dict.items():
        for tuples in orders:
            dishes.add(tuples[0])
    return dishes


def analyse_log(path_to_file):
    raise NotImplementedError
    # iniciando o projeto
