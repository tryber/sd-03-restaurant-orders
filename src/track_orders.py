class TrackOrders:
    def __init__(self):
        self.orders = []
        self.dishes_set = set()
        self.days_set = set()

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append([customer, order, day])
        self.dishes_set.add(order)
        self.days_set.add(day)

    def get_dishes_per_order(self, customer):
        dish_count = dict()
        for name, dish, _ in self.orders:
            if name == customer:
                if dish not in dish_count:
                    dish_count[dish] = 1
                else:
                    dish_count[dish] += 1
        return dish_count

    def get_days_per_order(self):
        day_count = dict()
        for _, _, day in self.orders:
            if day not in day_count:
                day_count[day] = 1
            else:
                day_count[day] += 1
        return day_count

    def get_most_ordered_dish_per_costumer(self, customer):
        dcpc = self.get_dishes_per_order(customer)
        return max(dcpc, key=dcpc.get)

    def get_order_frequency_per_costumer(self, customer, order):
        dcpc = self.get_dishes_per_order(customer)
        return dcpc[order]

    def get_never_ordered_per_costumer(self, customer):
        customer_dishes = set()
        for name, dish, _ in self.orders:
            if name == customer:
                customer_dishes.add(dish)
        return self.dishes_set.difference(customer_dishes)

    def get_days_never_visited_per_costumer(self, customer):
        customer_weekdays = set()
        for name, _, weekday in self.orders:
            if name == customer:
                customer_weekdays.add(weekday)
        return self.days_set.difference(customer_weekdays)

    def get_busiest_day(self):
        day_count = self.get_days_per_order()
        return max(day_count, key=day_count.get)

    def get_least_busy_day(self):
        day_count = self.get_days_per_order()
        return min(day_count, key=day_count.get)


if __name__ == "__main__":
    torders = TrackOrders()
    torders.add_new_order("jorge", "frango", "domingo")
    torders.add_new_order("jorge", "frango", "domingo")
    torders.add_new_order("arnaldo", "peixe", "sábado")
    torders.add_new_order("maria", "carne", "sábado")
    torders.add_new_order("joao", "salada", "segunda-feira")
    print(torders.get_least_busy_day())
    # print(torders.get_dishes_per_order('jorge'))
