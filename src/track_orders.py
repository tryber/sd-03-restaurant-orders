from src.analyze_log import most_frequent_per_client, never_asked


class TrackOrders:
    def __init__(self):
        self.orders = {}
        self.products = set()
        self.days_of_week = set()
        self.lenght = 0
        self.weekday_frequency = {}

    def __len__(self):
        return self.lenght

    def add_new_order(self, costumer, order, day):
        if costumer not in self.orders:
            self.orders[costumer] = [{"product": order, "day_of_week": day}]
        else:
            self.orders[costumer].append(
                {"product": order, "day_of_week": day})
        self.lenght += 1
        self.products.add(order)
        self.days_of_week.add(day)
        if day not in self.weekday_frequency:
            self.weekday_frequency[day] = 1
        else:
            self.weekday_frequency[day] += 1

    def get_most_ordered_dish_per_costumer(self, costumer):
        return most_frequent_per_client(self.orders, costumer, 'product')

    def get_order_frequency_per_costumer(self, costumer, order):
        count = 0

        for ordem in self.orders[costumer]:
            if ordem["product"] == order:
                count += 1

        return count

    def get_never_ordered_per_costumer(self, costumer):
        return never_asked(self.orders, costumer, self.products, 'product')

    def get_days_never_visited_per_costumer(self, costumer):
        return never_asked(
            self.orders, costumer, self.days_of_week, 'day_of_week')

    def get_busiest_day(self):
        most = list(self.weekday_frequency.keys())[0]
        for day in self.weekday_frequency:
            if self.weekday_frequency[day] > self.weekday_frequency[most]:
                most = day
        return most

    def get_least_busy_day(self):
        less = list(self.weekday_frequency.keys())[0]
        for day in self.weekday_frequency:
            if (self.weekday_frequency[day] < self.weekday_frequency[less]):
                less = day
        return less
