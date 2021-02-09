import csv
from collections import Counter


def format_csv(path_to_file):
    with open(path_to_file, "r") as file:
        file_data = csv.reader(file, delimiter=",", quotechar='"')
        data = [*file_data]
        return data


def count_item_by_custumer(orders, customer):
    orders_by_customer = []

    for name, order, week_day in orders:
        if name == customer:
            orders_by_customer.append(order)

    return Counter(orders_by_customer)


def get_customer_most_wanted(orders, customer):
    items = count_item_by_custumer(orders=orders, customer=customer)

    return items.most_common(1)[0][0]


def get_customer_item_quantity(orders, customer, item):
    return count_item_by_custumer(orders=orders, customer=customer)[item]


def get_menu(orders):
    menu = [order for name, order, week_day in orders]
    return set(menu)


def get_days(orders):
    days = [week_day for name, order, week_day in orders]
    return set(days)


def custumer_never_order(orders, customer):
    menu = get_menu(orders)
    orders = count_item_by_custumer(orders, customer)

    return set([order for order in menu if order not in orders])


def day_without_visit(orders, customer):
    days = get_days(orders)
    days_custumer_used = [week_day for name, order, week_day in orders
                          if name == customer]

    return set([day for day in days if day not in days_custumer_used])


def analyze_log(path_to_file):
    data = format_csv(path_to_file)

    maria_favorite = get_customer_most_wanted(data, "maria")
    arnaldo_hamburguers_quantity = get_customer_item_quantity(
        data,
        "arnaldo",
        "hamburguer"
        )
    joao_never_ordered = custumer_never_order(data, "joao")
    joao_not_gone_days = day_without_visit(data, "joao")
    file = open("./data/mkt_campaign.txt", "w")
    file.write(f"{maria_favorite}\n")
    file.write(f"{arnaldo_hamburguers_quantity}\n")
    file.write(f"{joao_never_ordered}\n")
    file.write(f"{joao_not_gone_days}\n")
