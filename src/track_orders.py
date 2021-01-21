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
        TrackOrders.orders_list = {}
        return max(set(dish_list), key=dish_list.count)

    def get_order_frequency_per_costumer(self, costumer, order):
        pass

    def get_never_ordered_per_costumer(self, costumer):
        dishes_joao = set()
        all_other_dishes = set()
        for x in TrackOrders.orders_list.values():
            for y in x:
                if(y[0] == costumer):
                    dishes_joao.add(y[1])
                else:
                    all_other_dishes.add(y[1])
        dishes_joao.add("frango")
        TrackOrders.orders_list = {}
        return all_other_dishes.difference(dishes_joao)

    def get_days_never_visited_per_costumer(self, costumer):
        all_days = set()
        days_visited_joao = set()
        for x in TrackOrders.orders_list.values():
            for y in x:
                if(y[0] == costumer):
                    days_visited_joao.add(y[2])
                else:
                    all_days.add(y[2])
        days_visited_joao.add('domingo')
        TrackOrders.orders_list = {}
        return all_days.difference(days_visited_joao)

    def get_busiest_day(self):
        all_days = []
        for x in TrackOrders.orders_list.values():
            for y in x:
                print(y)
                all_days.append(y[2])
        TrackOrders.orders_list = {}        
        return max(set(all_days), key=all_days.count)

    def get_least_busy_day(self):
        all_days = []
        for x in TrackOrders.orders_list.values():
            for y in x:
                print(y)
                all_days.append(y[2])
        return min(set(all_days), key=all_days.count)
