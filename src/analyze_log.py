import csv


def analyze_log(path_to_file):
    # prato mais pedido por maria
    # count arnaldo hamburgues
    # comida que joao nao pediu
    # dia que joao n foi
    with open(path_to_file) as file:
        raw_csv = csv.reader(file, delimiter=",")
        for item in raw_csv:
            print(item)
        return raw_csv


if __name__ == "__main__":
    # print(analyze_log("./data/orders_1.csv"))
    analyze_log("./data/orders_1.csv")
