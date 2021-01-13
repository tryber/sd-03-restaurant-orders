class TrackOrders:
    def __init__(self, path):
        self.orders = []
        self.orders_per_day = {}

    def __len__(self):
        return len(self.orders)

    def orders_per_day(self, day=False):
        if day:
            self.orders_per_day[day] += 1
        else:
            for order in self.orders:
                day = order["day"]
                if counter.get(day, 0):
                    self.orders_per_day[day] += 1
                else:
                    self.orders_per_day[day] = 1

    def add_new_order(self, costumer, order, day):
        order_dict = {"person": costumer, "item": order, "day": day}
        self.orders.append(order_dict)
        self.orders_per_day(day)

    def get_most_ordered_dish_per_costumer(self, costumer):
        most_ordered = ""
        counter = {}
        for order in self.orders:
            item = order["item"]
            if order["person"] == costumer:
                if counter.get(order["item"], 0):
                    counter[item] += 1
                else:
                    counter[item] = 1
            if not most_ordered or counter.get(item, 0) > counter.get(
                most_ordered, 0
            ):
                most_ordered = item
        return most_ordered

    def get_order_frequency_per_costumer(self, costumer, item):
        counter = 0
        for order in self.orders:
            if order["person"] == costumer and order["item"] == item:
                counter += 1
        return counter

    def get_never_ordered_per_costumer(self, costumer):
        menu = set()
        ordered_by_client = set()
        for order in self.orders:
            menu.add(order["item"])
            if order["person"] == costumer:
                ordered_by_client.add(order["item"])
        difference = menu.difference(ordered_by_client)
        return difference

    def get_days_never_visited_per_costumer(self, costumer):
        days = set()
        days_went = set()
        for order in self.orders:
            days.add(order["day"])
            if order["person"] == costumer:
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
        for day in self.orders_per_day:
            if (
                self.orders_per_day.get(busiest_day, 0)
                > self.orders_per_day[day]
            ):
                busiest_day = day
        return busiest_day


if __name__ == "__main__":
    analyze_log("data/orders_1.csv")
