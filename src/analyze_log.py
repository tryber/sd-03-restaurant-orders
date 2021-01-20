import csv


def get_most_consumed_dish(result):
    mariaDish = {}
    most_consumed_qty = 1
    most_consumed_dish = ""
    for arr in result:
        if arr[0] == "maria":
            if arr[1] not in mariaDish:
                mariaDish[arr[1]] = 1
            else:
                mariaDish[arr[1]] += 1
                if mariaDish[arr[1]] > most_consumed_qty:
                    most_consumed_qty = mariaDish[arr[1]]
                    most_consumed_dish = arr[1]
    return f"{str(most_consumed_dish)}\n"


def consumed_hamburguers_by_arnaldo(result):
    hamburher_consumed = 0
    for arr in result:
        if arr[0] == "arnaldo":
            if arr[1] == "hamburguer":
                hamburher_consumed += 1
    return f"{str(hamburher_consumed)}\n"


def never_ordered(result):
    dishes = set()
    joao_orders = set()
    not_ordered = set()
    for arr in result:
        dishes.add(arr[1])
        if arr[0] == "joao":
            joao_orders.add(arr[1])
    for i in dishes:
        if i not in joao_orders:
            not_ordered.add(i)
    return f"{str(not_ordered)}\n"


def never_gone(result):
    days = set()
    days_gone = set()
    days_not_gone = set()
    for arr in result:
        days.add(arr[2])
        if arr[0] == "joao":
            print('entrou')
            days_gone.add(arr[2])
    for i in days:
        if i not in days_gone:
            days_not_gone.add(i)      
    return str(days_not_gone)


def analyze_log(filepath):
    arr = []
    with open(filepath) as file:
        result = csv.reader(file, delimiter=";", quotechar='"')
        for row in result:
            arr.append(row[0].split(","))
    most_consumed_dish = get_most_consumed_dish(arr)
    consumed_hamburguers = consumed_hamburguers_by_arnaldo(arr)
    never_eaten = never_ordered(arr)
    days_not_gone = never_gone(arr)
    file = open("data/mkt_campaign.txt", mode="w")
    LINES = [
        most_consumed_dish,
        consumed_hamburguers,
        never_eaten,
        days_not_gone,
    ]
    file.writelines(LINES)
    file.close()


analyze_log('data/orders_1.csv')
