class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        most_requested = ""
        costumer_orders = {}

        for name, order, day in self.orders:
            if name == costumer:
                if order not in costumer_orders:
                    costumer_orders[order] = 1
                else:
                    costumer_orders[order] += 1

                if (
                    most_requested not in costumer_orders
                    or costumer_orders[order] > costumer_orders[most_requested]
                ):
                    most_requested = order

        return most_requested

    def get_order_frequency_per_costumer(self, costumer, order):
        quantity = 0

        for name, recipe, day in self.orders:
            if name == costumer and recipe == order:
                quantity += 1

        return quantity

    def get_never_ordered_per_costumer(self, costumer):
        restaurant_orders = set()
        costumer_orders = set()

        for name, order, day in self.orders:
            restaurant_orders.add(order)

            if name == costumer:
                costumer_orders.add(order)

        return restaurant_orders.difference(costumer_orders)

    def get_days_never_visited_per_costumer(self, costumer):
        open_days = set()
        visited_days = set()

        for name, order, day in self.orders:
            open_days.add(day)

            if name == costumer:
                visited_days.add(day)

        return open_days.difference(visited_days)

    def get_busiest_day(self):
        most_busiest_day = ""
        visited_days = {}

        for name, order, day in self.orders:
            if day not in visited_days:
                visited_days[day] = 1
            else:
                visited_days[day] += 1

            if (
                most_busiest_day not in visited_days
                or visited_days[day] > visited_days[most_busiest_day]
            ):
                most_busiest_day = day

        return most_busiest_day

    def get_least_busy_day(self):
        least_busy_day = ""
        visited_days = {}

        for name, order, day in self.orders:
            if day not in visited_days:
                visited_days[day] = 1
            else:
                visited_days[day] += 1

            if (
                least_busy_day not in visited_days
                or visited_days[day] < visited_days[least_busy_day]
            ):
                least_busy_day = day

        return least_busy_day


if __name__ == "__main__":
    tracker = TrackOrders()
    print(tracker.__len__())
    tracker.add_new_order("ana", "pizza", "domingo")
    tracker.add_new_order("maria", "misto-quente", "segunda-feira")
    tracker.add_new_order("joao", "misto-quente", "segunda-feira")
    print(tracker.get_most_ordered_dish_per_costumer("ana"))
    print(tracker.get_order_frequency_per_costumer("ana", "pizza"))
    print(tracker.get_never_ordered_per_costumer("ana"))
    print(tracker.get_days_never_visited_per_costumer("ana"))
    print(tracker.get_busiest_day())
    print(tracker.get_least_busy_day())
