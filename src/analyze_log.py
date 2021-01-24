import csv


def never_asked(orders, name, list_of, term):
    products = set()
    set_list = set(list_of)
    for order in orders[name]:
        products.add(order[term])
    return (set_list.difference(products))


def most_frequent_product_per_client(order_list, client):
    count = {}
    most_frequent = order_list[client][0]["product"]

    for order in order_list[client]:
        if order["product"] not in count:
            count[order["product"]] = 1
        else:
            count[order["product"]] += 1

        if count[order["product"]] > count[most_frequent]:
            most_frequent = order["product"]

    return most_frequent


def count_product_per_client(order_list, client):
    count = {}

    for order in order_list[client]:
        if order["product"] not in count:
            count[order["product"]] = 1
        else:
            count[order["product"]] += 1

    return count


def organize_list(csv):
    order_list = {}
    products = set()
    days_of_week = set()
    for name, product, day_of_week in csv:
        products.add(product)
        days_of_week.add(day_of_week)
        if name not in order_list:
            order_list[name] = [
                {"product": product, "day_of_week": day_of_week}]
        else:
            order_list[name].append(
                {"product": product, "day_of_week": day_of_week})
    return order_list, products, days_of_week


def read_csv(path_to_file):
    with open(path_to_file, "r") as file:
        csv_reader = csv.reader(file, delimiter=",", quotechar='"')
        organized_list = organize_list(csv_reader)
    return organized_list


def analyze_log(path_to_file):
    order_list, products, days_of_week = read_csv(path_to_file)
    maria_most_ordered_product = most_frequent_product_per_client(
        order_list, 'maria')
    arnaldo_hamburguer_orders = count_product_per_client(order_list, 'arnaldo')
    joao_never_asked_products = never_asked(
        order_list, 'joao', products, 'product')
    joao_never_asked_days_of_week = never_asked(
        order_list, 'joao', days_of_week, 'day_of_week')
    file = open("data/mkt_campaign.txt", "w")
    file.write(f"{maria_most_ordered_product}\n")
    file.write(f"{arnaldo_hamburguer_orders['hamburguer']}\n")
    file.write(f"{joao_never_asked_products}\n")
    file.write(f"{joao_never_asked_days_of_week}")
