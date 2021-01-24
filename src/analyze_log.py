from csv import reader


def get_data_from_csv(file):
    with open(file) as file:
        raw = reader(file, delimiter=",")
        data = []
        for customer, meal, day in raw:
            data.append([customer, meal, day])
    return data

def save_data_to_txt(file, food_data):
    with open(file, "w") as file:
        for data in food_data:
            file.write(f"{data}\n")

def times_ordered_by_customer(data, meal, customer):
        total = 0
        for item in data:
            if item[0] == customer and item[1] == meal:
                total += 1
        return total

def days_customer_missing(data, customer):
        days = set()
        days_went = set()
        for order in data:
            days.add(order[2])
            if order[0] == customer:
                days_went.add(order[2])
        difference = days.difference(days_went)
        return difference

def get_favorite_meal_by_customer(data, customer):
    meal_ordered_by_customer = {}
    for item in data:
        if item[0] == customer:
            if item[1] not in meal_ordered_by_customer.keys():
                meal_ordered_by_customer[item[1]] = 0
            if meal_ordered_by_customer[item[1]] >= 0:
                meal_ordered_by_customer[item[1]] += 1
    return max(meal_ordered_by_customer, key=meal_ordered_by_customer.get)


def meal_never_ordered(data, customer):
    meals_ordered = set()
    customer_ordered = set()
    for order in data:
        meals_ordered.add(order[1])
        if order[0] == customer:
            customer_ordered.add(order[1])
    return meals_ordered.difference(customer_ordered)


def analyze_log(path_to_file):
    data = get_data_from_csv(path_to_file)
    most_ordered = get_favorite_meal_by_customer(data, "maria")
    customer_missing_days = days_customer_missing(data, "joao")
    times_hamburger_ordered = times_ordered_by_customer(data, 'hamburguer', 'arnaldo')
    never_ordered_by = meal_never_ordered(data, 'joao')
    save_data_to_txt("./data/mkt_campaign.txt", [most_ordered, times_hamburger_ordered, never_ordered_by, customer_missing_days])
