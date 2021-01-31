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
        self.mkt_metrics["days"].setdefault(day, { "total": 0})
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
        pass

    def get_never_ordered_per_customer(self, customer):
        pass

    def get_days_never_visited_per_customer(self, customer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
