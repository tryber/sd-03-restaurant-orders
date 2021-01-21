import csv


def get_favorite_dish(file, person):
    favorite_food = ""
    for name, dish, day in file:
        if name == person:
            favorite_food = dish
    return favorite_food


def get_most_orders(file, person, recipe):
    count_recipe = 0
    for name, dish, day in file:
        if name == person and dish == recipe:
            print(dish, recipe)
            count_recipe += 1
    return str(count_recipe)


def get_never_request_dish(file, person):
    set_recipes = set()
    check_recipe_not_request = set()
    for name, dish, day in file:
        set_recipes.add(dish)
        if name == person:
            check_recipe_not_request.add(dish)

    return set_recipes.difference(check_recipe_not_request)


def get_days_not_visit(file, person):
    day_visit = set()
    day_not_visit = set()
    for name, dish, day in file:
        day_visit.add(day)
        if name == person:
            day_not_visit.add(day)

    return day_visit.difference(day_not_visit)


def analyse_log(path_to_file):
    with open(path_to_file, "r") as file:
        reader = csv.reader(file, delimiter=",")
# acuçar_sintático =
# https://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/
        new_reader = [*reader]
        dish_maria = get_favorite_dish(new_reader, "maria")
        arnaldo_most_hamburguer = get_most_orders(
            new_reader, "arnaldo", "hamburguer"
        )
        joao_never_request = get_never_request_dish(new_reader, "joao")
        joao_day_never_go = get_days_not_visit(new_reader, "joao")
        with open("data/mkt_campaign.txt", "w") as result_report:
            report = [
                dish_maria,
                arnaldo_most_hamburguer,
                joao_never_request,
                joao_day_never_go,
            ]
            result_report.writelines(report)
            result_report.close()
    return print(report)


if __name__ == "__main__":
    analyse_log("data/orders_1.csv")
