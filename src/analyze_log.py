import csv


def find_most_ordered_item_by_person(order_list, person):
    # prato mais pedido por maria
    return order_list[person]


def count_orders_by_food_and_person(order_list, food, person):
    # count arnaldo hamburgues
    return order_list


def foods_not_ordered_by_person(order_list, person):
    # comida que joao nao pediu
    return order_list


def days_that_one_person_didnt_go(order_list, person):
    # dia que joao n foi
    return order_list


def extract_orders_from_file(file):
    orders_list = {}
    raw_csv = csv.reader(file, delimiter=",")
    for person, food, day in raw_csv:
        if person not in orders_list:
            orders_list[person] = [food, day]
        else:
            orders_list[person].append(food)
            orders_list[person].append(day)
    return orders_list


def analyze_log(path_to_file):
    with open(path_to_file) as file:
        orders_list = extract_orders_from_file(file)
        return find_most_ordered_item_by_person(orders_list, 'maria')


if __name__ == "__main__":
    print(analyze_log("./data/orders_1.csv"))
    # analyze_log("./data/orders_1.csv")
