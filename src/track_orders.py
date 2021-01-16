class TrackOrders:
    def __init__(self):
        self.orders = []
        self.dish_count = dict()
        self.day_count = dict()
        self.dishes_set = set()
        self.days_set = set()

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append([customer, order, day])
        self.dishes_set.add(order)
        self.days_set.add(day)
        if day not in self.day_count:
            self.day_count[day]: 1
        else:
            self.day_count[day] += 1

    def get_dishes_per_customers(self, customer):
        for name, dish, _ in self.orders:
            if name == customer:
                if dish not in self.dish_count:
                    self.dish_count[dish] = 1
                else:
                    self.dish_count[dish] += 1

    def get_most_ordered_dish_per_customer(self, customer):
        self.get_dishes_per_customers(self. customer)
        return max(self.dish_count, key=self.dish_count.get)

    def get_order_frequency_per_customer(self, customer, order):
        self.get_dishes_per_customers(self. customer)
        return self.dish_count[order]

    def get_never_ordered_per_customer(self, customer):
        customer_dishes = set()
        for name, dish, _ in self.orders:
            if name == customer:
                customer_dishes.add(dish)
        return self.dishes_set.difference(customer_dishes)

    def get_days_never_visited_per_customer(self, customer):
        customer_weekdays = set()
        for name, _, weekday in self.orders:
            if name == customer:
                customer_weekdays.add(weekday)
        return self.days_set.difference(customer_weekdays)

    def get_busiest_day(self):
        return max(self.day_count, key=self.day_count.get)

    def get_least_busy_day(self):
        return min(self.day_count, key=self.day_count.get)
