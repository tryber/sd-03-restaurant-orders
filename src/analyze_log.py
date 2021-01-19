import csv


def analyze_csv_lines(path_to_file):
    return (more_ask_maria(path_to_file) + "\n"
            + f'{how_many_tymes_arnaldo_ask(path_to_file)}' + "\n"
            + f'{dish_joao_dont_ask(path_to_file)}' + "\n"
            + f'{dates_joao_do_not_go_restaurant(path_to_file)}'
            )


def more_ask_maria(path_to_file):
    file_content = read_file(path_to_file)
    only_maria_cardapio = []
    for row in file_content:
        if row[0] == "maria":
            only_maria_cardapio.append(row[1])
    # https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/        
    return (max(set(only_maria_cardapio), key=only_maria_cardapio.count))


def how_many_tymes_arnaldo_ask(path_to_file):
    only_arnaldo_ask_hamburguer = []
    file_content = read_file(path_to_file)
    for row in file_content:
        if row[0] == "arnaldo" and row[1] == "hamburguer":
            print("test")
            only_arnaldo_ask_hamburguer.append(row[1])
    return len(only_arnaldo_ask_hamburguer)


def dish_joao_dont_ask(path_to_file):
    file_content = read_file(path_to_file)
    joao_ask = set()
    receipts = set()
    for row in file_content:
        if row[0] == "joao":
            joao_ask.add(row[1])
        else:
            receipts.add(row[1])

    return receipts.difference(joao_ask)


def dates_joao_do_not_go_restaurant(path_to_file):
    file_content = read_file(path_to_file)
    joao_dates = set()
    all_dates = set()
    for row in file_content:
        if row[0] == "joao":
            joao_dates.add(row[2])
        else:
            all_dates.add(row[2])

    return all_dates.difference(joao_dates)


def read_file(path_to_file):
    file_content = " "
    csv_file = open(path_to_file)
    file_content = csv.reader(csv_file, delimiter=",")
    return file_content


def analyze_log(path_to_file):
    txt_file = open("data/mkt_campaign.txt", "a")
    txt_file.write(analyze_csv_lines(path_to_file))


# analyze_log("/home/cpereiramt/Documentos/Projetos/python/sd-03-restaurant-orders/data/orders_1.csv")
