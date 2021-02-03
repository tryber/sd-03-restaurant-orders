import csv


def format_data(path_to_file):
    with open(path_to_file, "r") as file:
        file_content = csv.reader(file, delimiter=",", quotechar='"')
        data = [*file_content]
        return data


def get_favorite_disth(orders, customer):
    most_requested = ""
    orders_dict = {}
    for name, order, day in orders:
        if name == customer:
            if order not in orders_dict:
                orders_dict[order] = 1
            else:
                orders_dict[order] += 1

            if (
                most_requested not in orders_dict
                or orders_dict[order] > orders_dict[most_requested]
            ):
                most_requested = order

    return most_requested


def get_orders(orders, item, customer):
    quantity_by_item = 0

    for name, order, day in orders:
        if name == customer and order == item:
            quantity_by_item += 1

    return quantity_by_item


def what_dishes_never_ordered(orders, customer):
    dishes = set()
    recipe_not_request = set()

    for name, order, day in orders:
        if name == customer:
            recipe_not_request.add(order)
        dishes.add(order)

    return dishes.difference(recipe_not_request)


def get_days_not_visit(orders, customer):
    days = set()
    days_not_visit = set()

    for name, order, day in orders:
        if name == customer:
            days_not_visit.add(day)
        days.add(day)

    return days.difference(days_not_visit)


def analyze_log(path_to_file):
    data = format_data(path_to_file)
    dish_maria = get_favorite_disth(data, "maria")
    arnaldo_most_hamburguers = get_orders(
        data,
        "hamburguer",
        "arnaldo"
    )
    joao_never_request = what_dishes_never_ordered(data, "joao")
    joao_day_never_go = get_days_not_visit(data, "joao")
    file = open("./data/mkt_campaign.txt", "w")
    file.write(f"{dish_maria}\n")
    file.write(f"{arnaldo_most_hamburguers}\n")
    file.write(f"{joao_never_request}\n")
    file.write(f"{joao_day_never_go}\n")
