import csv


def parse_data(path):
    data = {
        'menu': set(),
        'week_days': set()
    }
    with open(path) as file:
        reader = csv.reader(file, delimiter=",", quotechar='"')
        for costumer, order, day in reader:
            data["menu"].add(order)
            data["week_days"].add(day)
            if costumer not in data:
                data[costumer] = {"orders": [order], "days": [day]}
            else:
                data[costumer]["orders"].append(order)
                data[costumer]["days"].append(day)
    return data


def most_ordered(costumer, data):
    orders_dict = dict()
    orders = data[costumer]['orders']
    for order in orders:
        if order not in orders_dict:
            orders_dict[order] = 1
        else:
            orders_dict[order] += 1

    sort_orders = sorted(orders_dict.items(), key=lambda x: x[1], reverse=True)

    return sort_orders[0][0]


def specific_order(costumer, data, specific):
    orders_dict = dict()
    orders = data[costumer]['orders']
    for order in orders:
        if order not in orders_dict:
            orders_dict[order] = 1
        else:
            orders_dict[order] += 1

    return orders_dict[specific]


def analyze_log(path_to_file):
    data = parse_data(path_to_file)
    menu = data["menu"]
    wd = data["week_days"]

    maria_most_ordered = most_ordered('maria', data)
    arnaldos_hamburguer = specific_order('arnaldo', data, 'hamburguer')
    joao_not_orders = menu.difference(data['joao']['orders'])
    joao_not_days = wd.difference(data['joao']['days'])

    with open("data/mkt_campaign.txt", mode="w") as file:
        file.write(f"{str(maria_most_ordered)}\n")
        file.write(f"{str(arnaldos_hamburguer)}\n")
        file.write(f"{str(joao_not_orders)}\n")
        file.write(f"{str(joao_not_days)}\n")
