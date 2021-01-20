import csv


def eats(data, person):
    favorite_food = ""
    asked_foods = {}
    for name, order, day in data:
        if name == person:
            if order not in asked_foods:
                asked_foods[order] = 1
            else:
                asked_foods[order] += 1
    favorite_food = max(asked_foods, key=asked_foods.get)
    return favorite_food


def person_asked_hamburguer(data, person):
    times = 0
    for name, order, day in data:
        if name == person and order == 'hamburguer':
            times += 1
    return times


def person_never_asked(data, person):
    foods = set()
    person_order = set()
    for name, order, day in data:
        foods.add(order)
        if name == person:
            person_order.add(order)
    return foods-person_order


def person_never_went(data, person):
    days = set()
    person_went = set()
    for name, order, day in data:
        days.add(day)
        if name == person:
            person_went.add(day)
    return days.difference(person_went)


def analyze_log(path_to_file):
    with open(path_to_file, "r") as orders_file:
        content = csv.reader(orders_file, delimiter=",")
        data = [*content]
        maria_eats = eats(data, 'maria')
        arnaldo_ask_hamburguer = person_asked_hamburguer(data, 'arnaldo')
        joao_never_ask = person_never_asked(data, 'joao')
        joao_never_went = person_never_went(data, 'joao')
    with open("data/mkt_campaign.txt", "w") as file_txt_file:
        print(
            maria_eats,
            arnaldo_ask_hamburguer,
            joao_never_ask,
            joao_never_went,
            sep="\n",
            file=file_txt_file,
        )
