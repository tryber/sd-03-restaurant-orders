class TrackOrders:
    def __init__(self):
        self.data_dict = dict()
        self.data_list = list()
        self.menu = set()
        self.wd = set()

    def __len__(self):
        return len(self.data_list)

    def add_new_order(self, costumer, order, day):
        self.data_list.append([costumer, order, day])
        self.menu.add(order)
        self.wd.add(day)
        if costumer not in self.data_dict:
            self.data_dict[costumer] = {"orders": [order], "days": [day]}
        else:
            self.data_dict[costumer]["orders"].append(order)
            self.data_dict[costumer]["days"].append(day)

    def get_most_ordered_dish_per_costumer(self, costumer):
        orders_dict = dict()
        orders = self.data_dict[costumer]['orders']
        for order in orders:
            if order not in orders_dict:
                orders_dict[order] = 1
            else:
                orders_dict[order] += 1

        sort_orders = sorted(
            orders_dict.items(), key=lambda x: x[1], reverse=True)

        return sort_orders[0][0]

    def get_order_frequency_per_costumer(self, costumer, order):
        orders_dict = dict()
        orders = self.data_dict[costumer]['orders']
        for order in orders:
            if order not in orders_dict:
                orders_dict[order] = 1
            else:
                orders_dict[order] += 1

        return orders_dict[order]

    def get_never_ordered_per_costumer(self, costumer):
        return self.menu.difference(self.data_dict[costumer]['orders'])

    def get_days_never_visited_per_costumer(self, costumer):
        return self.wd.difference(self.data_dict[costumer]['days'])

    def get_busiest_day(self):
        days_dict = dict()
        for order in self.data_list:
            if order[2] not in days_dict:
                days_dict[order[2]] = 1
            else:
                days_dict[order[2]] += 1

        sort_days = sorted(
            days_dict.items(), key=lambda x: x[1], reverse=True)

        return sort_days[0][0]

    def get_least_busy_day(self):
        days_dict = dict()
        for order in self.data_list:
            if order[2] not in days_dict:
                days_dict[order[2]] = 1
            else:
                days_dict[order[2]] += 1

        sort_days = sorted(
            days_dict.items(), key=lambda x: x[1], reverse=False)

        return sort_days[0][0]
