import csv


def file_organizer(file):
    orders = {}
    days = set()
    foods = set()
    raw_csv = csv.reader(file, delimiter=",")
    for person, food, day in raw_csv:
        days.add(day)
        foods.add(food)
        if person not in orders:
            orders[person] = [food, day]
        else:
            orders[person].append(food)
            orders[person].append(day)
    data = {"orders": orders, "days": days, "foods": foods}
    return data


def list_counter(unsorted_list):
    sorted_dict = {}
    for item in unsorted_list:
        if item not in sorted_dict:
            sorted_dict[item] = 1
        else:
            sorted_dict[item] += 1
    return sorted_dict


def dict_counter(unsorted_dict):
    sorted_dict = {}
    for name in unsorted_dict:
        sorted_dict[name] = list_counter(unsorted_dict[name])
    return sorted_dict


def find_most_ordered_by_person():
    return


def analyze_log(path_to_file):
    orders_data = {}
    orders = {}
    foods = set()
    # days = set()
    # log = []
    with open(path_to_file) as file:
        orders_data = file_organizer(file)
        orders = dict_counter(orders_data['orders'])
        foods = orders_data['foods']
        # days = orders_data['days']
        # pprint(foods)
        # pprint(days)

    # prato mais pedido por maria
    # find_most_ordered_by_person()
    test = foods.intersection(orders['maria'])
    test1 = {}
    for food in test:
        test1[food] = orders['maria'][food]
    print(test1)
    # count arnaldo hamburgues
    # comida que joao nao pediu
    # dia que joao n foi
    return orders


if __name__ == "__main__":
    # pprint(analyze_log("./data/orders_1.csv"))
    analyze_log('./data/orders_1.csv')
