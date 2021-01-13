import csv
from pprint import pprint


def dict_maker(file):
    order_by_person = {}
    raw_csv = csv.reader(file, delimiter=",")
    for person, food, day in raw_csv:
        if person not in order_by_person:
            order_by_person[person] = [food, day]
        else:
            order_by_person[person].append(food)
            order_by_person[person].append(day)
    return order_by_person


def list_counter(unsorted_list):
    sorted_list = {}
    for elem in unsorted_list:
        if elem not in sorted_list:
            sorted_list[elem] = 1
        else:
            sorted_list[elem] += 1
    return sorted_list


def analyze_log(path_to_file):
    try:
        person_dict = {}
        with open(path_to_file) as file:
            person_dict = dict_maker(file)
            # pprint(person_dict)
            keys_dict = person_dict.keys()
            for key in keys_dict:
                person_dict[key] = list_counter(person_dict[key])
        return person_dict
    except FileNotFoundError:
        # print(f"No such file or directory: {path_to_file}")
        return f"No such file or directory: {path_to_file}"


if __name__ == "__main__":
    pprint(analyze_log('./data/orders_1.csv'))
    # analyze_log('./data/orders_1.csv')
