from src.analyze_log import best_seller_by_client
from src.analyze_log import dish_frequency_by_client
from src.analyze_log import never_ordered
from src.analyze_log import never_be_in_day
from src.analyze_log import all_dishes
from src.analyze_log import all_days


class TrackOrders:
    def __init__(self):
        self.orders = {}
        self.dishes = set()
        self.days = set()
        self.count = {}
        self.list_of_days = list()
        self.most_frequent = ""
        self.least_frequent = ""

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        if costumer not in self.orders:
            self.orders[costumer] = [(order, day)]
        else:
            self.orders[costumer].append((order, day))

    def get_most_ordered_dish_per_costumer(self, costumer):
        return best_seller_by_client(costumer, self.orders)

    def get_order_frequency_per_costumer(self, costumer, order):
        return dish_frequency_by_client(costumer, order, self.orders)

    def get_never_ordered_per_costumer(self, costumer):
        self.dishes = all_dishes(self.orders)
        return never_ordered(costumer, self.dishes, self.orders)

    def get_days_never_visited_per_costumer(self, costumer):
        self.days = all_days(self.orders)
        return never_be_in_day(costumer, self.days, self.orders)

    def get_busiest_day(self):
        self.days = all_days(self.orders)
        self.list_of_days = list(self.days)
        self.most_frequent = self.list_of_days[0]

        for day in self.list_of_days:
            self.count[day] = 1

        for costumer, order_list in self.orders.items():
            for tuples in order_list:
                self.count[tuples[1]] += 1

                if self.count[tuples[1]] > self.count[self.most_frequent]:
                    self.most_frequent = tuples[1]

        return self.most_frequent

    def get_least_busy_day(self):
        self.days = all_days(self.orders)
        self.list_of_days = list(self.days)
        self.least_frequent = self.list_of_days[0]

        for day in self.list_of_days:
            self.count[day] = 1

        for costumer, order_list in self.orders.items():
            for tuples in order_list:
                self.count[tuples[1]] += 1

                if self.count[tuples[1]] < self.count[self.least_frequent]:
                    self.least_frequent = tuples[1]

        return self.least_frequent
