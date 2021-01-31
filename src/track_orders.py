class TrackOrders:
    def __init__(self):
        self.mkt_metrics = { }
        self.menu = set()
        self.working_days = set()
        self.orders = set()

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.menu.add(order)
        self.working_days.add(day)
        self.orders.add((costumer, order, day))
        
        self.mkt_metrics.setdefault(costumer, {})
        self.mkt_metrics[costumer].setdefault(order, {"total": 0})
        self.mkt_metrics[costumer][order].setdefault(day, 0)
        self.mkt_metrics.setdefault("days", {})
        self.mkt_metrics["days"].setdefault(day, { "total": 0})
        self.mkt_metrics["days"][day].setdefault(costumer, {})
        self.mkt_metrics["days"][day][costumer].setdefault(order, 0)

        self.mkt_metrics[costumer][order][day] += 1
        self.mkt_metrics[costumer][order]["total"] += 1
        self.mkt_metrics["days"][day]["total"] += 1
        self.mkt_metrics["days"][day][costumer][order] += 1

    def get_most_ordered_dish_per_costumer(self, costumer):
        pass

    def get_order_frequency_per_costumer(self, costumer, order):
        pass

    def get_never_ordered_per_costumer(self, costumer):
        pass

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
