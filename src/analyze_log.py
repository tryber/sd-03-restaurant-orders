import csv


# Baseado no código de Gabryel Ryba em
# https://github.com/tryber/sd-03-restaurant-orders/blob/
# gabryelryba-restaurant-orders/src/analyze_log.py
def format_data(row, orders):
    if (row[0] not in orders.keys()):
        orders[row[0]] = {'dishes': {}, 'date':  {}}


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


def top_order_per_costumer(orders, costumer):
    return max(orders[costumer]['dishes'], key=orders[costumer]['dishes'].get)


def never_ordered_per_costumer(dishes, costumer, orders=[]):
    return dishes - orders[costumer]['dishes'].keys()


def never_visited_per_costumer(days, costumer, orders=[]):
    return days - orders['joao']['date'].keys()

def analyse_log(path_to_file):
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
            format_data(row, orders)
            save_dishes(row, orders)
            save_date(row, orders)

        maria = top_order_per_costumer(orders, 'maria')
        arnaldo = orders['arnaldo']['dishes']['hamburguer'] or 0
        order = never_ordered_per_costumer(dishes, 'joao', orders)
        day = never_visited_per_costumer(days, 'joao', orders)

        with open('data/mkt_campaign.txt', mode='w') as costumer_analysis:
            costumer_analysis.writelines(
                f'{maria}\n{arnaldo}\n{order}\n{day}\n')
