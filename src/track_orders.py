from analyze_log import (
    get_most_requested_recipe,
    get_qnt_the_recipe_was_ordered,
    get_recipes_never_ordered,
    get_unvisited_days
)


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        return get_most_requested_recipe(self.orders, costumer)

    def get_order_frequency_per_costumer(self, costumer, order):
        return get_qnt_the_recipe_was_ordered(self.orders, costumer, order)

    def get_never_ordered_per_costumer(self, costumer):
        return get_recipes_never_ordered(self.orders, costumer)

    def get_days_never_visited_per_costumer(self, costumer):
        return get_unvisited_days(self.orders, costumer)

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass


if __name__ == "__main__":
    tracker = TrackOrders()
    print(tracker.__len__())
    tracker.add_new_order("ana", "pizza", "domingo")
    tracker.add_new_order("maria", "sopa", "segunda-feira")
    print(tracker.get_most_ordered_dish_per_costumer("ana"))
    print(tracker.get_order_frequency_per_costumer("ana", "pizza"))
    print(tracker.get_never_ordered_per_costumer("ana"))
    print(tracker.get_days_never_visited_per_costumer("ana"))
