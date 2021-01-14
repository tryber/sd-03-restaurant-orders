<<<<<<< HEAD
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


def never_ordered_by_client(foods_from_person, query_person):
    # comida que joao nao pediu
    all_foods = set()
    for person in foods_from_person:
        for food in foods_from_person[person]:
            all_foods.add(food)
    return all_foods.difference(foods_from_person[query_person])


def days_that_one_person_didnt_go(days_from_person, query_person):
    # dia que joao n foi
    all_days = set()
    for person in days_from_person:
        for day in days_from_person[person]:
            all_days.add(day)
    return all_days.difference(days_from_person[query_person])


def extract_food_from_file_by_person(data):
    orders_by_food = {}
    for person, food, day in data:
        if person not in orders_by_food:
            orders_by_food[person] = [food]
        else:
            orders_by_food[person].append(food)
    return orders_by_food


def extract_day_from_file_by_person(data):
    orders_by_day = {}
    for person, food, day in data:
        if person not in orders_by_day:
            orders_by_day[person] = [day]
        else:
            orders_by_day[person].append(day)
    return orders_by_day


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
    foods_from_person = extract_food_from_file_by_person(data)
    days_from_person = extract_day_from_file_by_person(data)
    most_ordered = client_favorite_order(foods_from_person, "maria")
    how_many_orders = count_orders_by_food_and_person(
        foods_from_person, "hamburguer", "arnaldo"
    )
    food_not_ordered = never_ordered_by_client(foods_from_person, "joao")
    absent_days = days_that_one_person_didnt_go(days_from_person, "joao")
    save_data(
        "./data/mkt_campaign.txt",
        [most_ordered, how_many_orders, food_not_ordered, absent_days],
    )


if __name__ == "__main__":
    analyze_log("./data/orders_1.csv")
    # analyze_log("./data/orders_1.csv")
