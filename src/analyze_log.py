import csv


def get_most_requested_recipe(data, costumer):
    most_requested = ""
    costumer_orders = {}

    for name, order, day in data:
        if name == costumer:
            if order not in costumer_orders:
                costumer_orders[order] = 1
            else:
                costumer_orders[order] += 1

            if (
                most_requested not in costumer_orders
                or costumer_orders[order] > costumer_orders[most_requested]
            ):
                most_requested = order

    return most_requested


def get_qnt_the_recipe_was_ordered(data, costumer, recipe):
    quantity = 0

    for name, order, day in data:
        if name == costumer and order == recipe:
            quantity += 1

    return quantity


def get_recipes_never_ordered(data, costumer):
    restaurant_recipes = set()
    costumer_recipes = set()

    for name, order, day in data:
        restaurant_recipes.add(order)

        if name == costumer:
            costumer_recipes.add(order)

    return restaurant_recipes.difference(costumer_recipes)


def get_unvisited_days(data, costumer):
    open_days = set()
    visited_days = set()

    for name, order, day in data:
        open_days.add(day)

        if name == costumer:
            visited_days.add(day)

    return open_days.difference(visited_days)


def analyze_log(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise ValueError(f"No such file or directory: {path_to_file}")

    try:
        with open(path_to_file, "r") as orders_file:
            content = csv.reader(orders_file, delimiter=",")
            data = [*content]

            most_requested_recipe = get_most_requested_recipe(data, "maria")
            qnt_the_recipe_was_ordered = get_qnt_the_recipe_was_ordered(
                data, "arnaldo", "hamburguer"
            )
            recipes_never_ordered = get_recipes_never_ordered(data, "joao")
            unvisited_days = get_unvisited_days(data, "joao")

            with open("data/mkt_campaign.txt", "w") as marketing_file:
                print(
                    most_requested_recipe,
                    qnt_the_recipe_was_ordered,
                    recipes_never_ordered,
                    unvisited_days,
                    sep="\n",
                    file=marketing_file
                )
    except FileNotFoundError:
        raise ValueError(f"No such file or directory: {path_to_file}")


if __name__ == "__main__":
    analyze_log("data/orders_1.csv")
