import csv


def person_most_frequent_meal(all_data, person):
    count = {}
    most_frequent_meal = all_data[person]["food"][0]

    for meal in all_data[person]["food"]:
        if meal not in count:
            count[meal] = 1
        else:
            count[meal] += 1

        if count[meal] > count[most_frequent_meal]:
            most_frequent_meal = meal

    return most_frequent_meal


def person_meal_count(all_data, person, order):
    count = 0

    for meal in all_data[person]["food"]:
        if meal == order:
            count += 1

    return count


def person_meal_never_ordered(meals_type, persons_meal):
    person_differents_meals = set(persons_meal)

    unordered_meals_by_person = meals_type.difference(person_differents_meals)

    return unordered_meals_by_person


def person_days_without_going(days_of_the_week, persons_days_going):
    different_persons_going_day = set(persons_days_going)

    without_going_days = days_of_the_week.difference(
        different_persons_going_day
    )

    return without_going_days


def analyze_log(path_to_file):
    with open(path_to_file) as file:
        readable = csv.reader(file, delimiter=",", quotechar='"')
        data_in_dict = {
            "foods_types": set(),
            "days_of_week": set(),
        }

        for customer, order, day in readable:
            data_in_dict["foods_types"].add(order)
            data_in_dict["days_of_week"].add(day)
            if customer not in data_in_dict:
                data_in_dict[customer] = {"food": [order], "day": [day]}
            else:
                data_in_dict[customer]["food"].append(order)
                data_in_dict[customer]["day"].append(day)

        most_frequent_meal = person_most_frequent_meal(data_in_dict, "maria")

        hamburguer_count = person_meal_count(
            data_in_dict, "arnaldo", "hamburguer"
        )

        meals_never_ordered = person_meal_never_ordered(
            data_in_dict["foods_types"], data_in_dict["joao"]["food"]
        )

        days_without_going = person_days_without_going(
            data_in_dict["days_of_week"], data_in_dict["joao"]["day"]
        )

        with open("data/mkt_campaign.txt", mode="w") as file:
            file.write(f"{str(most_frequent_meal)}\n")
            file.write(f"{str(hamburguer_count)}\n")
            file.write(f"{str(meals_never_ordered)}\n")
            file.write(f"{str(days_without_going)}\n")


if __name__ == "__main__":
    print(analyze_log("./data/orders_1.csv"))
