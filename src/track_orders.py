class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        favorite_food = ""
        asked_foods = {}
        for name, order, day in self.orders:
            if name == costumer:
                if order not in asked_foods:
                    asked_foods[order] = 1
                else:
                    asked_foods[order] += 1
        favorite_food = max(asked_foods, key=asked_foods.get)
        print(favorite_food)
        return favorite_food

    def get_order_frequency_per_costumer(self, costumer, order):
        pass

    def get_never_ordered_per_costumer(self, costumer):
        foods = set()
        person_order = set()
        for name, order, day in self.orders:
            foods.add(order)
            if name == costumer:
                person_order.add(order)
        return foods-person_order

    def get_days_never_visited_per_costumer(self, costumer):
        days = set()
        person_went = set()
        for name, order, day in self.orders:
            days.add(day)
            if name == costumer:
                person_went.add(day)
        return days.difference(person_went)

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
