import csv
# import os


def create_order_base(row, orders):
    if (row[0] not in orders.keys()):
        orders[row[0]] = {
            'dishes': {},
            'date':  {}
        }


def save_dishes(row, orders):
    if row[1] not in orders[row[0]]['dishes'].keys():
        orders[row[0]]['dishes'][row[1]] = 1
    else:
        orders[row[0]]['dishes'][row[1]] += 1


def save_date(row, orders):
    if row[2] not in orders[row[0]]['date'].keys():
        orders[row[0]]['date'][row[2]] = 1
    else:
        orders[row[0]]['date'][row[2]] += 1


def get_most_ordered_dish_per_costumer(orders, costumer):
    return max(orders[costumer]['dishes'], key=orders[costumer]['dishes'].get)


def get_never_ord(dishes, costumer, orders=[]):
    return dishes - orders[costumer]['dishes'].keys()


def get_never_visited(days, costumer, orders=[]):
    return days - orders['joao']['date'].keys()


def analyze_log(path_to_file):
    dishes = set()
    days = set()
    orders = dict()
    orders['work_days'] = set()
    orders['dishes_list'] = set()
    with open(path_to_file, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            dishes.add(row[1])
            days.add(row[2])
            create_order_base(row, orders)
            save_dishes(row, orders)
            save_date(row, orders)

        file.close()

        maria = get_most_ordered_dish_per_costumer(orders, 'maria')
        arnaldo = orders['arnaldo']['dishes']['hamburguer'] or 0
        joao_never_ord = get_never_ord(dishes, 'joao', orders)
        joao_never_day = get_never_visited(days, 'joao', orders)

        with open('data/mkt_campaign.txt', mode='w') as text_result:
            text_result.writelines(
                f'{maria}\n{arnaldo}\n{joao_never_ord}\n{joao_never_day}\n')
            text_result.close()


if __name__ == '__main__':
    analyze_log('data/orders_1.csv')
