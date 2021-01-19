class TrackOrders:
    orders_list = {}

    def __len__(self):
        return len(TrackOrders.orders_list)

    def add_new_order(self, costumer, order, day):
        TrackOrders.orders_list[costumer] = [order, day]        
        print(TrackOrders.orders_list)

    def get_most_ordered_dish_per_costumer(self, costumer):
        pass
        return 0

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
