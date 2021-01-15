import csv


def get_qnt_by_recipe(requests, person):
    qnt_by_recipe = {}
    for name, recipe, day in requests:
        if name == person:
            qnt_by_recipe[recipe] = qnt_by_recipe.get(recipe, 0) + 1

    return max(qnt_by_recipe, key=qnt_by_recipe.get)


def get_qnt_of_recipe(requests, person, specified_recipe):
    qnt_by_person_recipe = 0
    for name, recipe, day in requests:
        if name == person and recipe == specified_recipe:
            qnt_by_person_recipe += 1

    return qnt_by_person_recipe


def get_never_requested_recipe(requests, person):
    requesteds_recipes = set()
    all_requesteds_recipes = set()
    for name, recipe, day in requests:
        all_requesteds_recipes.add(recipe)
        if name == person:
            requesteds_recipes.add(recipe)

    return all_requesteds_recipes.difference(requesteds_recipes)


def get_not_visited_day(requests, person):
    open_days = set()
    visited_days = set()

    for name, recipe, day in requests:
        open_days.add(day)

        if name == "joao":
            visited_days.add(day)

    return open_days.difference(visited_days)


def analyze_log(path_to_file):
    with open(path_to_file) as file:
        requests = csv.reader(file, delimiter=",")
        recs = [*requests]
        most_requested_recipe = get_qnt_by_recipe(recs, "maria")
        qnt_recipe = get_qnt_of_recipe(recs, "arnaldo", "hamburguer")
        not_requesteds_recipes = get_never_requested_recipe(recs, "joao")
        not_visited_days = get_not_visited_day(recs, "joao")

        with open("data/mkt_campaign.txt", "w") as mkfile:
            print(
                most_requested_recipe,
                qnt_recipe,
                not_requesteds_recipes,
                not_visited_days,
                sep="\n",
                file=mkfile,
            )


if __name__ == "__main__":
    analyze_log("data/orders_1.csv")
