import csv


def analyze_log(path_to_file):
    with open(path_to_file) as csv_file:
        file_content = csv.reader(csv_file, delimiter=",")
        for row in file_content:
            print(row)


# analyse_log("/home/cpereiramt/Documentos/Projetos/python/sd-03-restaurant-orders/data/orders_1.csv")
