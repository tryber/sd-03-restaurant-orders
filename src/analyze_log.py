import csv


def best_seller_by_client(client, dict):
    # cada cliente retorne uma lista de tuplas onde o
    # prato é o primeiro elemento
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


def dish_frequency_by_client(client, dish, dict):
    # cada cliente retorne uma lista de tuplas onde o
    # prato é o primeiro elemento
    count = {}
    client_list = dict[client]
    for dish, day in client_list:
        if dish not in count:
            count[dish] = 1
        else:
            count[dish] += 1

    return count[dish]


def all_dishes(dict):
    dishes = set()
    for client, orders in dict.items():
        for tuples in orders:
            dishes.add(tuples[0])
    return dishes


def all_days(dict):
    days = set()
    for client, orders in dict.items():
        for tuples in orders:
            days.add(tuples[1])
    return days


def never_ordered(client, dishes, dict):
    client_list = dict[client]
    client_dishes = set()

    for orders in client_list:
        client_dishes.add(orders[0])

    return dishes.difference(client_dishes)


def never_be_in_day(client, days, dict):
    client_list = dict[client]
    client_days = set()

    for orders in client_list:
        client_days.add(orders[1])

    return days.difference(client_days)


def save_lines_in_txt(filepath, lines):
    with open(filepath, "w") as file:
        for line in lines:
            file.writelines(f"{line}\n")


def analyse_log(path_to_file):
    data = {}

    # Popula o dicionario data
    if not path_to_file.endswith('.csv'):
        raise ValueError('Arquivo inválido')
    with open(path_to_file) as csv_file:
        csv_dict = csv.reader(csv_file, delimiter=",")
        for name, dish, day in csv_dict:
            if name not in data:
                data[name] = [(dish, day)]
            else:
                data[name].append((dish, day))

    dishes = all_dishes(data)
    days = all_days(data)
    analysis = []

    analysis.append(best_seller_by_client("maria", data))
    analysis.append(dish_frequency_by_client("arnaldo", "hamburger", data))
    analysis.append(never_ordered("joao", dishes, data))
    analysis.append(never_be_in_day("joao", days, data))

    save_lines_in_txt("../data/mkt_campaign.txt", analysis)


if __name__ == "__main__":
    analyse_log("../data/orders_1.csv")
