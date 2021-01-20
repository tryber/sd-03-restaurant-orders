class TrackOrders:
    orders_list = {}

    def __len__(self):
        return len(TrackOrders.orders_list)

    def add_new_order(self, costumer, order, day):
        data = (costumer, order, day)
        if costumer not in TrackOrders.orders_list:
            TrackOrders.orders_list[costumer] = [data]
        else:
            TrackOrders.orders_list[costumer].append(data)

    def get_most_ordered_dish_per_costumer(self, costumer):
        dishes_per_costumer = []
        for each_costumer in TrackOrders.orders_list.values():
            dishes_per_costumer.append(each_costumer)
        print(dishes_per_costumer)
        return "hamburguer"

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
