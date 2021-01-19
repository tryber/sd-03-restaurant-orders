import csv


def analyse_log(path_to_file):
    orders = dict()
    orders['work_days'] = set()
    orders['dishes_list'] = set()
    with open(path_to_file, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            orders['dishes_list'].add(row[1])
            orders['work_days'].add(row[2])
            if (row[0] not in orders.keys()):
                orders[row[0]] = {
                    'dishes': {},
                    'date':  {}
                }

            if row[1] not in orders[row[0]]['dishes'].keys():
                orders[row[0]]['dishes'][row[1]] = 1
            else:
                orders[row[0]]['dishes'][row[1]] += 1

            if row[2] not in orders[row[0]]['date'].keys():
                orders[row[0]]['date'][row[2]] = 1
            else:
                orders[row[0]]['date'][row[2]] += 1
        file.close()

        # pprint.pprint(orders)
        maria = max(orders['maria']['dishes'],
                    key=orders['maria']['dishes'].get)
        arnaldo = orders['arnaldo']['dishes']['hamburguer'] or 0
        joao = orders['dishes_list'] - orders['joao']['dishes'].keys()
        joao_never = orders['work_days'] - orders['joao']['date'].keys()

        with open('data/mkt_campaign.txt', mode='w') as text_result:
            text_result.writelines(
                f'{maria};\n{arnaldo};\n{joao};\n{joao_never}\n')
            text_result.close()


if __name__ == '__main__':
    analyse_log('data/orders_1.csv')
