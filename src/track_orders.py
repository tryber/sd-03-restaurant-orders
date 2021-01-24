class TrackOrders:
    def __init__(self):
        self.orders = []
        self.orders_per_day = {}

    def __len__(self):
        return len(self.orders)

    def orders_per_day(self, day):
        if self.orders_per_day[day]:
            self.orders_per_day[day] += 1
        else:
            self.orders_per_day[day] = 1

    def add_new_order(self, customer, order, day):
        order_dict = {"customer": customer, "item": order, "day": day}
        self.orders.append(order_dict)
        if self.orders_per_day.get(day):
            self.orders_per_day[day] += 1
        else:
            self.orders_per_day[day] = 1

    def get_most_ordered_dish_per_costumer(self, customer):
        most_ordered = ""
        total = {}
        for order in self.orders:
            item = order["item"]
            if order["customer"] == customer:
                if total.get(order["item"], 0):
                    total[item] += 1
                else:
                    total[item] = 1
            if not most_ordered or total.get(item, 0) > total.get(
                most_ordered, 0
            ):
                most_ordered = item
        return most_ordered

    def get_order_frequency_per_costumer(self, customer, item):
        total = 0
        for order in self.orders:
            if order["customer"] == customer and order["item"] == item:
                total += 1
        return total

    def get_never_ordered_per_costumer(self, customer):
        menu = set()
        ordered_by_client = set()
        for order in self.orders:
            menu.add(order["item"])
            if order["customer"] == customer:
                ordered_by_client.add(order["item"])
        difference = menu.difference(ordered_by_client)
        return difference

    def get_days_never_visited_per_costumer(self, customer):
        days = set()
        days_went = set()
        for order in self.orders:
            days.add(order["day"])
            if order["customer"] == customer:
                days_went.add(order["day"])
        difference = days.difference(days_went)
        return difference

    def get_busiest_day(self):
        busiest_day = ""
        for day in self.orders_per_day:
            if (
                self.orders_per_day.get(busiest_day, 0)
                < self.orders_per_day[day]
            ):
                busiest_day = day
        return busiest_day

    def get_least_busy_day(self):
        busiest_day = ""
        for day in self.orders_per_day:
            if self.orders_per_day.get(
                busiest_day, 1
            ) >= self.orders_per_day.get(day):
                busiest_day = day
        return busiest_day
