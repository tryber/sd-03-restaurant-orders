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
        dishes_maria_tuple = []
        dish_list = []
        for costumer_each in TrackOrders.orders_list.values():
            if costumer in costumer_each[0]:
                dishes_maria_tuple.append(costumer_each)
        for x in dishes_maria_tuple:
            for y in x:
                dish_list.append(y[1])
        return max(set(dish_list), key=dish_list.count)

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
