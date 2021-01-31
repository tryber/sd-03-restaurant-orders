import csv


def most_ordered_food(mkt_metrics, customer):
    most_ordered_food = ""
    total_ordered = 0
    for food in mkt_metrics[customer]:
        if mkt_metrics[customer][food]["total"] > total_ordered:
            total_ordered = mkt_metrics[customer][food]["total"]
            most_ordered_food = food
    return most_ordered_food


def unpopular_foods(mkt_metrics, menu, customer):
    unpopular_foods = set()
    for food in menu:
        if not mkt_metrics[customer].get(food):
            unpopular_foods.add(food)
    return unpopular_foods


def unpopular_days(mkt_metrics, working_days, customer):
    unpopular_days = set()
    for day in working_days:
        if not mkt_metrics["days"][day].get(customer):
            unpopular_days.add(day)
    return unpopular_days


def create_mkt_analysis_dict(orders):
    mkt_metrics = {}
    menu = set()
    working_days = set()
    for name, food, day in orders:
        menu.add(food)
        working_days.add(day)
        mkt_metrics.setdefault(name, {})
        mkt_metrics[name].setdefault(food, {"total": 0})
        mkt_metrics[name][food].setdefault(day, 0)
        mkt_metrics.setdefault("days", {})
        mkt_metrics["days"].setdefault(day, {})
        mkt_metrics["days"][day].setdefault(name, {})
        mkt_metrics["days"][day][name].setdefault(food, 0)
        mkt_metrics[name][food][day] += 1
        mkt_metrics[name][food]["total"] += 1
        mkt_metrics["days"][day][name][food] += 1
    return (mkt_metrics, menu, working_days)


def analyze_log(path_to_file):
    with open(path_to_file) as file:
        orders = csv.reader(file, delimiter=",")
        mkt_metrics, menu, working_days = create_mkt_analysis_dict(orders)

    most_ordered_food_maria = most_ordered_food(mkt_metrics, "maria")

    total_hamburguers_arnaldo = mkt_metrics["arnaldo"]["hamburguer"]["total"]

    unpopular_foods_joao = unpopular_foods(mkt_metrics, menu, "joao")

    unpopular_days_joao = unpopular_days(mkt_metrics, working_days, "joao")

    with open("data/mkt_campaign.txt", "w") as file:
        file.write(f"""{most_ordered_food_maria}
{total_hamburguers_arnaldo}
{unpopular_foods_joao}
{unpopular_days_joao}""")


if __name__ == "__main__":
    analyse_log('../data/orders_1.csv')
