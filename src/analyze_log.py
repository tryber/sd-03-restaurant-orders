import csv


def get_maria_info(path_to_file):
    maria_dish = ""
    maria_orders = {}

    with open(path_to_file, "r") as file:
        data = csv.reader(file, delimiter=",", quotechar='"')

        for name, order, day in data:
            if name == "maria":
                if order not in maria_orders:
                    maria_orders[order] = 1
                else:
                    maria_orders[order] += 1

                if (
                    maria_dish not in maria_orders
                    or maria_orders[order] > maria_orders[maria_dish]
                ):
                    maria_dish = order

        return maria_dish


def get_arnaldo_info(path_to_file):
    arnaldo_frequency = 0

    with open(path_to_file, "r") as file:
        data = csv.reader(file, delimiter=",", quotechar='"')

        for name, order, day in data:
            if name == "arnaldo" and order == "hamburguer":
                arnaldo_frequency += 1

    return str(arnaldo_frequency)


def format_output(data):
    tamanho = len(data)
    string = "{"
    for index, item in enumerate(data, 1):
        string += str(item)
        if index != tamanho:
            string += ", "
    string += "}"
    return string


def get_joao_info(path_to_file):
    restaurant_dishes = set()
    joao_dishes = set()
    restaurant_days = set()
    joao_days = set()

    with open(path_to_file, "r") as file:
        data = csv.reader(file, delimiter=",", quotechar='"')

        for name, order, day in data:
            restaurant_dishes.add(order)
            restaurant_days.add(day)

            if name == "joao":
                joao_dishes.add(order)
                joao_days.add(day)

    dishes_never = restaurant_dishes.difference(joao_dishes)
    days_never_went_to_restaurant = restaurant_days.difference(joao_days)

    return [
        format_output(dishes_never),
        format_output(days_never_went_to_restaurant),
    ]


def analyse_log(path_to_file):
    maria_dish = get_maria_info(path_to_file)
    arnaldo_frequency = get_arnaldo_info(path_to_file)
    (
        dishes_never_ordered_by_joao,
        days_that_joao_never_went_to_restaurant,
    ) = get_joao_info(path_to_file)

    result = [
        maria_dish + ";\n",
        arnaldo_frequency + ";\n",
        dishes_never_ordered_by_joao + ";\n",
        days_that_joao_never_went_to_restaurant,
    ]

    with open("data/mkt_campaign.txt", "w") as file:
        file.writelines(result)
