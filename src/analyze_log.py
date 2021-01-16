import csv


def client_favorite_order(foods_from_person, person):
    # prato mais pedido por maria
    foods_dict = {}
    most_ordered = foods_from_person[person][0]
    for food in foods_from_person[person]:
        if food not in foods_dict:
            foods_dict[food] = 1
        else:
            foods_dict[food] += 1
        if foods_dict[most_ordered] < foods_dict[food]:
            most_ordered = food
    return most_ordered


def count_orders_by_food_and_person(foods_from_person, query_food, person):
    # count arnaldo hamburgues
    orders_by_food = {}
    for food in foods_from_person[person]:
        if food not in orders_by_food:
            orders_by_food[food] = 1
        else:
            orders_by_food[food] += 1
    return orders_by_food[query_food]


def difference_by_person(data_from_people, query_person):
    # comida que joao nao pediu
    complete_set = set()
    for person in data_from_people:
        for individual_data in data_from_people[person]:
            complete_set.add(individual_data)
    return complete_set.difference(data_from_people[query_person])


def extract_specific_information(data_list, index):
    orders = {}
    for data in data_list:
        if data[0] not in orders:
            orders[data[0]] = [data[index]]
        else:
            orders[data[0]].append(data[index])
    return orders


def get_data(path_to_file):
    with open(path_to_file) as file:
        raw_data = csv.reader(file, delimiter=",")
        data = []
        for person, food, day in raw_data:
            data.append([person, food, day])
    return data


def save_data(path_to_file, data_list):
    with open(path_to_file, "w") as file:
        for data in data_list:
            file.write(f"{data}\n")


def analyze_log(path_to_file):
    most_ordered = ""
    how_many_orders = 0
    food_not_ordered = set()
    absent_days = set()
    data = get_data(path_to_file)

    foods_from_person = extract_specific_information(data, 1)
    days_from_person = extract_specific_information(data, 2)

    most_ordered = client_favorite_order(foods_from_person, "maria")
    how_many_orders = count_orders_by_food_and_person(
        foods_from_person, "hamburguer", "arnaldo"
    )
    food_not_ordered = difference_by_person(foods_from_person, "joao")
    absent_days = difference_by_person(days_from_person, "joao")
    save_data(
        "./data/mkt_campaign.txt",
        [most_ordered, how_many_orders, food_not_ordered, absent_days],
    )


if __name__ == "__main__":
    analyze_log("./data/orders_1.csv")
    # analyze_log("./data/orders_1.csv")
