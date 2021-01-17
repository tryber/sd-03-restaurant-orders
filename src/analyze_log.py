import csv


def get_dishes_per_customers(orders, customer):
    dcpc = {}  # Dish Count Per Customer
    for dish, _ in orders[customer]:
        if dish not in dcpc:
            dcpc[dish] = 1
        else:
            dcpc[dish] += 1
    return dcpc


def get_most_ordered_dish_per_customer(orders, customer):
    dish_count = get_dishes_per_customers(orders, customer)
    return max(dish_count, key=dish_count.get)


def get_order_frequency_per_customer(orders, customer, order):
    dish_count = get_dishes_per_customers(orders, customer)
    return dish_count[order]


def get_never_ordered_per_customer(customer_data, all_dishes):
    customer_dishes = set()
    for dish, _ in customer_data:
        customer_dishes.add(dish)
    return all_dishes.difference(customer_dishes)


def get_days_never_visited_per_customer(customer_data, all_weekdays):
    customer_weekdays = set()
    for _, weekday in customer_data:
        customer_weekdays.add(weekday)
    return all_weekdays.difference(customer_weekdays)


def analyse_log(path_to_file):
    try:
        obc = {}  # Orders By Customer
        dishes_set = set()
        days_set = set()
        with open(path_to_file, encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for customer, food, day in csv_reader:
                dishes_set.add(food)
                days_set.add(day)
                if customer not in obc:
                    obc[customer] = [[food, day]]
                else:
                    obc[customer].append([food, day])
        # Retorna um conjunto cuja chave é o nome do cliente e os valores
        # representam os ítens e seus respectivos dias da semana consumidos

        maria_favourite = get_most_ordered_dish_per_customer(obc, 'maria')
        abc = get_order_frequency_per_customer(obc, 'arnaldo', 'hamburguer')
        # Arnaldo Burguer Count

        nobj = get_never_ordered_per_customer(obc['joao'], dishes_set)
        # Not Ordered By Joao

        djwa = get_days_never_visited_per_customer(obc['joao'], days_set)
        # Days Joao was absent

        report = open('../data/mkt_campaign.txt', 'w')
        report.write(f'{maria_favourite};\n\n')
        report.write(f'{abc};\n\n')
        report.write(f'{nobj};\n\n')
        report.write(f'{djwa};')
        report.close()

    except FileNotFoundError:
        return f'No such file or directory: {path_to_file}'


if __name__ == '__main__':
    analyse_log('../data/orders_1.csv')
