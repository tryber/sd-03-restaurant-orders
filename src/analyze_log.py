from os import path
import csv


def import_data_people(filepath):
    if path.splitext(filepath)[1] != '.csv':
        raise FileNotFoundError(f"No such file or directory: '{filepath}'")
    with open(filepath) as file:
        data = csv.reader(file, delimiter=",", quotechar='"')
        orders = dict()
        for customer, order, day in data:
            if customer in orders:
                orders[customer].append([order, day])
            else:
                orders[customer] = [[order, day]]
        return orders


def import_data_food(filepath):
    with open(filepath) as file:
        data = csv.reader(file, delimiter=",", quotechar='"')
        food_list = set()
        for row in data:
            if row[1] not in food_list:
                food_list.add(row[1])
        return food_list


def import_data_days(filepath):
    with open(filepath) as file:
        data = csv.reader(file, delimiter=",", quotechar='"')
        days_list = set()
        for row in data:
            if row[2] not in days_list:
                days_list.add(row[2])
        return days_list


def maria_most_frequent(orders):
    foods = {}
    most_frequent = orders[0][0]
    for order in orders:
        if order[0] not in foods:
            foods[order[0]] = 1
        else:
            foods[order[0]] += 1

        if foods[order[0]] > foods[most_frequent]:
            most_frequent = order[0]

    return most_frequent


def arnaldo_hamburguer(orders):
    counter = 0
    for order in orders:
        if order[0] == "hamburguer":
            counter += 1
    return counter


def joao_orders(orders, filepath):
    restaurant_food = import_data_food(filepath)
    joao_food = set()
    for order in orders:
        if order[0] not in joao_food:
            joao_food.add(order[0])
    return restaurant_food.difference(joao_food)


def joao_never(orders, filepath):
    restaurant_days = import_data_days(filepath)
    joao_days = set()
    for order in orders:
        if order[1] not in joao_days:
            joao_days.add(order[1])
    return restaurant_days.difference(joao_days)


def analyze_log(path_to_file):
    orders = import_data_people(path_to_file)
    file_txt = open("data/mkt_campaign.txt", mode="w")

    maria = maria_most_frequent(orders["maria"])
    arnaldo = arnaldo_hamburguer(orders["arnaldo"])
    joao_food = joao_orders(orders["joao"], path_to_file)
    joao_days = joao_never(orders["joao"], path_to_file)

    file_txt.write(f"{maria}\n")
    file_txt.write(f"{arnaldo}\n")
    file_txt.write(f"{joao_food}\n")
    file_txt.write(f"{joao_days}\n")
    file_txt.close()
