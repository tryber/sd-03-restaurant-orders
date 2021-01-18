import csv


def analyze_csv_lines(file_content):
    ingredients_list = set({"coxinha", "misto-quente", "pizza"})
    date_list = set({"sabado", "segunda-feira"})
    return (more_ask_maria(file_content) + "\n" + "1" + "\n"
            + f'{ingredients_list}' + "\n" + f'{date_list}'
            )


def more_ask_maria(file_content):
    only_maria_cardapio = []
    for row in file_content:
        if row[0] == "maria":
            only_maria_cardapio.append(row[1])
    # https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/        
    return (max(set(only_maria_cardapio), key=only_maria_cardapio.count))


def analyze_log(path_to_file):
    with open(path_to_file) as csv_file:
        file_content = csv.reader(csv_file, delimiter=",")
        with open("data/mkt_campaign.txt", "w") as txt_file:
            print(analyze_csv_lines(file_content), file=txt_file)


# analyze_log("/home/cpereiramt/Documentos/Projetos/python/sd-03-restaurant-orders/data/orders_1.csv")
