import csv


def analyze_log(path_to_file):
    with open(path_to_file) as file:
        requests = csv.reader(file, delimiter=",")
        qnt_by_recipe = {}
        qnt_by_person_recipe = 0
        requesteds_recipes = set()
        all_requesteds_recipes = set()
        open_days = set()
        visited_days = set()

        for name, recipe, day in requests:
            all_requesteds_recipes.add(recipe)
            open_days.add(day)
            if name == "maria":
                qnt_by_recipe[recipe] = qnt_by_recipe.get(recipe, 0) + 1

            if name == "arnaldo" and recipe == "hamburguer":
                qnt_by_person_recipe += 1

            if name == "joao":
                requesteds_recipes.add(recipe)

            if name == "joao":
                visited_days.add(day)

        biggest_qnt = 0
        most_requested_recipe = ""
        for recipe, qnt in qnt_by_recipe.items():
            if qnt > biggest_qnt:
                biggest_qnt = qnt
                most_requested_recipe = recipe

        not_requesteds_recipes = all_requesteds_recipes.difference(
            requesteds_recipes
        )

        not_visited_days = open_days.difference(visited_days)

    with open("data/mkt_campaign.txt", "w") as mkfile:
        print(
            most_requested_recipe,
            qnt_by_person_recipe,
            not_requesteds_recipes,
            not_visited_days,
            sep="\n",
            file=mkfile,
        )


if __name__ == "__main__":
    analyze_log("data/orders_1.csv")
