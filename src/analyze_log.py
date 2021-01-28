import csv


def format_data(path_to_file):
    with open(path_to_file, "r") as file:
        file_content = csv.reader(file, delimiter=",", quotechar='"')
        data = [*file_content]
        return data


def most_requested_item_by_customer(orders, customer):
    most_requested = ""
    orders_dict = {}
    for name, order, week_day in orders:
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


def quantity_item_by_customer(orders, item, customer):
    quantity_by_item = 0

    for name, order, week_day in orders:
        if name == customer and order == item:
            quantity_by_item += 1

    return quantity_by_item


def dishes_never_ordered(orders, customer):
    # admitindo que o log contém a totalidade do cardápio
    dishes = set()
    customer_orders = set()

    for name, order, week_day in orders:
        if name == customer:
            customer_orders.add(order)
        dishes.add(order)

    return dishes.difference(customer_orders)


def days_never_frequented(orders, customer):
    days = set()
    days_frequented = set()

    for name, order, week_day in orders:
        if name == customer:
            days_frequented.add(week_day)
        days.add(week_day)

    return days.difference(days_frequented)


def analyse_log(path_to_file):
    raise NotImplementedError


if __name__ == "__main__":
    print(format_data("./data/orders_1.csv"))
    print(
        most_requested_item_by_customer(
            format_data("./data/orders_1.csv"), "maria"
        )
    )
    print(
        quantity_item_by_customer(
            format_data("./data/orders_1.csv"), "hamburguer", "arnaldo"
        )
    )
    print(dishes_never_ordered(format_data("./data/orders_1.csv"), "joao"))
    print(days_never_frequented(format_data("./data/orders_1.csv"), "joao"))
