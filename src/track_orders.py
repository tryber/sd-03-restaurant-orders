class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        mariaDish = {}
        most_consumed_qty = 1
        most_consumed_dish = ""
        for arr in self.orders:
            if arr[0] == costumer:
                if arr[1] not in mariaDish:
                    mariaDish[arr[1]] = 1
                else:
                    mariaDish[arr[1]] += 1
                    if mariaDish[arr[1]] > most_consumed_qty:
                        most_consumed_qty = mariaDish[arr[1]]
                        most_consumed_dish = arr[1]
        return most_consumed_dish

    def get_order_frequency_per_costumer(self, costumer, order):
        consumed = 0
        for arr in self.orders:
            if arr[0] == costumer:
                if arr[1] == order:
                    consumed += 1
        return consumed

    def get_never_ordered_per_costumer(self, costumer):
        dishes = set()
        joao_orders = set()
        not_ordered = set()
        for arr in self.orders:
            dishes.add(arr[1])
            if arr[0] == costumer:
                joao_orders.add(arr[1])
        for i in dishes:
            if i not in joao_orders:
                not_ordered.add(i)
        return not_ordered

    def get_days_never_visited_per_costumer(self, costumer):
        days = set()
        days_gone = set()
        days_not_gone = set()
        for arr in self.orders:
            days.add(arr[2])
            if arr[0] == costumer:
                days_gone.add(arr[2])
        for i in days:
            if i not in days_gone:
                days_not_gone.add(i)
        print(days)
        print(days_gone)
        return days_not_gone

    def get_busiest_day(self):
        days = {}
        busiest_count = 0
        busiest = ""
        for order in self.orders:
            if order[2] in days:
                days[order[2]] += 1
                if days[order[2]] > busiest_count:
                    busiest_count = days[order[2]]
                    busiest = order[2]
            else:
                days[order[2]] = 1
        return busiest

    def get_least_busy_day(self):
        days = {}
        for order in self.orders:
            if order[2] in days:
                days[order[2]] += 1
            else:
                days[order[2]] = 1
        min = 100000
        least = ""
        for day, count in days.items():
            if count < min:
                least = day
                min = count
        return least
