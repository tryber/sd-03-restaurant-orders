import csv


def get_total_dish(file, person):
    total_dish = {}
    for name, order, day in file:
        if name == person:
            total_dish[order]

    return len(total_dish)


def analyse_log(path_to_file):
    if not path_to_file:
        return FileNotFoundError
    if not path_to_file.endswith('.csv'):
        raise ValueError('Arquivo inválido')
    with open(path_to_file) as f:
        file = csv.reader(f, delimiter=",")
        result_dish = get_total_dish(file, "maria")
        with open("data/mkt/campaign.txt", "w"):
            print(result_dish)
