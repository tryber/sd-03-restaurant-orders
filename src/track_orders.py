class TrackOrders:
    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        pass

    def get_order_frequency_per_costumer(self, costumer, order):
        quantity = 0

        for name, recipe, day in self.orders:
            if name == costumer and recipe == order:
                quantity += 1

        return quantity

    def get_never_ordered_per_costumer(self, costumer):
        orders = set()
        costumer_orders = set()

        for name, order, day in self.orders:
            orders.add(order)

            if name == costumer:
                costumer_orders.add(order)

        return orders.difference(costumer_orders)

    def get_days_never_visited_per_costumer(self, costumer):
        days_on = set()
        days_with_people = set()

        for name, order, day in self.orders:
            days_on.add(day)

            if name == costumer:
                days_with_people.add(day)

        return days_on.difference(days_with_people)

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass

#Test