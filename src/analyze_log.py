import csv


def analyse_log(path_to_file):
    data = {}
    if not path_to_file.endswith('.csv'):
        raise ValueError('Arquivo inválido')
    with open(path_to_file) as csv_file:
        csv_dict = csv.reader(csv_file, delimiter=",")
        for name, dish, day in csv_dict:
            if name not in data:
                data[name] = [(dish, day)]
            else:
                data[name].append((dish, day))
    print(data)


analyse_log('../data/orders_1.csv')
