from collections import Counter


def count_item_by_custumer(orders, customer):
    orders_by_customer = []

    for name, order, week_day in orders:
        if name == customer:
            orders_by_customer.append(order)

    return Counter(orders_by_customer)


def count_days(orders):
    days = [week_day for name, order, week_day in orders]

    return Counter(days)


def get_customer_most_wanted(orders, customer):
    items = count_item_by_custumer(orders=orders, customer=customer)

    return items.most_common(1)[0][0]


def get_customer_item_quantity(orders, customer, item):
    return count_item_by_custumer(orders=orders, customer=customer)[item]


def get_menu(orders):
    menu = [order for name, order, week_day in orders]
    return set(menu)


def get_days(orders):
    days = [week_day for name, order, week_day in orders]
    return set(days)


def custumer_never_order(orders, customer):
    menu = get_menu(orders)
    orders = count_item_by_custumer(orders, customer)

    return set([order for order in menu if order not in orders])


def day_without_visit(orders, customer):
    days = get_days(orders)
    days_custumer_used = [week_day for name, order, week_day in orders
                          if name == customer]

    return set([day for day in days if day not in days_custumer_used])


class TrackOrders:

    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        return get_customer_most_wanted(self.orders, costumer)

    def get_order_frequency_per_costumer(self, costumer, order):
        return get_customer_item_quantity(self.orders, costumer, order)

    def get_never_ordered_per_costumer(self, costumer):
        return custumer_never_order(self.orders, costumer)

    def get_days_never_visited_per_costumer(self, costumer):
        return day_without_visit(self.orders, costumer)

    def get_busiest_day(self):
        return count_days(self.orders).most_common()[0][0]

    def get_least_busy_day(self):
        return count_days(self.orders).most_common()[-1][0]
