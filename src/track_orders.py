class TrackOrders:
    def __init__(self):
        self.mkt_metrics = {}
        self.menu = set()
        self.working_days = set()
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.menu.add(order)
        self.working_days.add(day)
        self.orders.append((customer, order, day))
        self.create_mkt_analysis((customer, order, day))

    def create_mkt_analysis(self, new_order):
        customer, order, day = new_order
        self.mkt_metrics.setdefault(customer, {})
        self.mkt_metrics[customer].setdefault(order, {"total": 0})
        self.mkt_metrics[customer][order].setdefault(day, 0)
        self.mkt_metrics.setdefault("days", {})
        self.mkt_metrics["days"].setdefault(day, {"total": 0})
        self.mkt_metrics["days"][day].setdefault(customer, {})
        self.mkt_metrics["days"][day][customer].setdefault(order, 0)
        self.mkt_metrics[customer][order][day] += 1
        self.mkt_metrics[customer][order]["total"] += 1
        self.mkt_metrics["days"][day]["total"] += 1
        self.mkt_metrics["days"][day][customer][order] += 1

    def get_most_ordered_dish_per_customer(self, customer):
        most_ordered_dish = ""
        total_ordered = 0
        for food in self.mkt_metrics[customer]:
            if self.mkt_metrics[customer][food]["total"] > total_ordered:
                total_ordered = self.mkt_metrics[customer][food]["total"]
                most_ordered_dish = food
        return most_ordered_dish

    def get_order_frequency_per_customer(self, customer, order):
        order_frequency = set()
        for food in self.mkt_metrics[customer]:
            total_ordered = self.mkt_metrics[customer][food]["total"]
            order_frequency.add((food, total_ordered))
        return order_frequency

    def get_never_ordered_per_customer(self, customer):
        unpopular_foods = set()
        for food in self.menu:
            if not self.mkt_metrics[customer].get(food):
                unpopular_foods.add(food)
        return unpopular_foods

    def get_days_never_visited_per_customer(self, customer):
        unpopular_days = set()
        for day in self.working_days:
            if not self.mkt_metrics["days"][day].get(customer):
                unpopular_days.add(day)
        return unpopular_days

    def get_busiest_day(self):
        busiest_day = ""
        biggest_frequency = 0
        for day in self.working_days:
            if self.mkt_metrics["days"][day]["total"] > biggest_frequency:
                busiest_day = day
                biggest_frequency = self.mkt_metrics["days"][day]["total"]
        return busiest_day

    def get_least_busy_day(self):
        unpopular_day = ""
        lowest_frequency = None
        for day in self.working_days:
            if not lowest_frequency:
                lowest_frequency = self.mkt_metrics["days"][day]["total"]
            if self.mkt_metrics["days"][day]["total"] < lowest_frequency:
                unpopular_day = day
                lowest_frequency = self.mkt_metrics["days"][day]["total"]
        return unpopular_day
