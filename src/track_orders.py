class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append([customer, order, day])

    def sort_orders_per_customer(self):
        orders = dict()
        for customer, food, day in self.orders:
            if customer in orders:
                orders[customer].append([food, day])
            else:
                orders[customer] = [[food, day]]
        return orders

    def get_most_ordered_dish_per_costumer(self, customer):
        orders_per_customer = self.sort_orders_per_customer()
        orders = orders_per_customer[customer]
        foods = {}
        most_frequent = orders[0][0]
        for order, _ in orders:
            if order not in foods:
                foods[order] = 1
            else:
                foods[order] += 1

            if foods[order] > foods[most_frequent]:
                most_frequent = order

        return most_frequent

    def get_order_frequency_per_costumer(self, costumer, order):
        pass

    def get_restaurant_food(self):
        food_list = set()
        for _, food, _ in self.orders:
            if food not in food_list:
                food_list.add(food)
        return food_list

    def get_never_ordered_per_costumer(self, customer):
        restaurant_food = self.get_restaurant_food()
        orders_per_customer = self.sort_orders_per_customer()
        orders = orders_per_customer[customer]
        customer_food = set()

        for food, _ in orders:
            if food not in customer_food:
                customer_food.add(food)

        return restaurant_food.difference(customer_food)

    def get_restaurant_days(self):
        days_list = set()
        for _, _, day in self.orders:
            if day not in days_list:
                days_list.add(day)
        return days_list

    def get_days_never_visited_per_costumer(self, customer):
        restaurant_days = self.get_restaurant_days()
        orders_per_customer = self.sort_orders_per_customer()
        orders = orders_per_customer[customer]
        customer_days = set()

        for _, day in orders:
            if day not in customer_days:
                customer_days.add(day)

        return restaurant_days.difference(customer_days)

    def get_busiest_day(self):
        days = {}
        busiest_day = self.orders[0][2]

        for _, _, day in self.orders:
            if day not in days:
                days[day] = 1
            else:
                days[day] += 1

            if days[day] > days[busiest_day]:
                busiest_day = day

        return busiest_day

    def get_least_busy_day(self):
        days = {}
        least_busiest_day = self.orders[0][2]

        for _, _, day in self.orders:
            if day not in days:
                days[day] = 1
            else:
                days[day] += 1

            if days[day] < days[least_busiest_day]:
                least_busiest_day = day

        return least_busiest_day
