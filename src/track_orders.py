class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        most_requested = ""
        orders_dict = {}
        for name, order, week_day in self.orders:
            if name == costumer:
                if order not in orders_dict:
                    orders_dict[order] = 1
                else:
                    orders_dict[order] += 1

                if (
                    most_requested not in orders_dict
                    or orders_dict[order] > orders_dict[most_requested]
                ):
                    most_requested = order

        return most_requested

    def get_order_frequency_per_costumer(self, costumer, order):
        quantity_by_item = 0

        for name, item, week_day in self.orders:
            if name == costumer and item == order:
                quantity_by_item += 1

        return quantity_by_item

    def get_never_ordered_per_costumer(self, costumer):
        dishes = set()
        customer_orders = set()

        for name, order, week_day in self.orders:
            if name == costumer:
                customer_orders.add(order)
            dishes.add(order)

        return dishes.difference(customer_orders)

    def get_days_never_visited_per_costumer(self, costumer):
        days = set()
        days_frequented = set()

        for name, order, week_day in self.orders:
            if name == costumer:
                days_frequented.add(week_day)
            days.add(week_day)

        return days.difference(days_frequented)

    def get_busiest_day(self):
        busiest_day = ""
        business_days = {}
        for name, order, week_day in self.orders:
            if week_day not in business_days:
                business_days[week_day] = 1
            else:
                business_days[week_day] += 1

            if (
                busiest_day not in business_days
                or business_days[week_day] > business_days[busiest_day]
            ):
                busiest_day = week_day

        return busiest_day

    def get_least_busy_day(self):
        lazyest_day = ""
        business_days = {}
        for name, order, week_day in self.orders:
            if week_day not in business_days:
                business_days[week_day] = 1
            else:
                business_days[week_day] += 1

            if (
                lazyest_day not in business_days
                or business_days[week_day] < business_days[lazyest_day]
            ):
                lazyest_day = week_day

        return lazyest_day
