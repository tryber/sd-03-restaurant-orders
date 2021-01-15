from src.analyze_log import (
    person_most_frequent_meal,
    person_meal_count,
    person_meal_never_ordered,
    person_days_without_going,
)


class TrackOrders:
    def __init__(self):
        self._foods_type = set()
        self._days_of_week = set()
        self._orders_per_client = {}
        self._days_count = {}
        self._count_orders = 0

    def __len__(self):
        return self._count_orders

    def add_new_order(self, costumer, order, day):
        self._count_orders += 1
        self._foods_type.add(order)
        self._days_of_week.add(day)
        if costumer not in self._orders_per_client:
            self._orders_per_client[costumer] = {"food": [order], "day": [day]}
        else:
            self._orders_per_client[costumer]["food"].append(order)
            self._orders_per_client[costumer]["day"].append(day)

        if day not in self._days_count:
            self._days_count[day] = 1
        else:
            self._days_count[day] += 1

    def get_most_ordered_dish_per_costumer(self, costumer):
        return person_most_frequent_meal(self._orders_per_client, costumer)

    def get_order_frequency_per_costumer(self, costumer, order):
        return person_meal_count(self._orders_per_client, costumer, order)

    def get_never_ordered_per_costumer(self, costumer):
        return person_meal_never_ordered(
            self._foods_type, self._orders_per_client[costumer]["food"]
        )

    def get_days_never_visited_per_costumer(self, costumer):
        return person_days_without_going(
            self._days_of_week, self._orders_per_client[costumer]["day"]
        )

    def get_busiest_day(self):
        day_count = 0
        busiest_day = ""

        for day in self._days_count:
            if self._days_count[day] > day_count:
                day_count = self._days_count[day]
                busiest_day = day

        return busiest_day

    def get_least_busy_day(self):
        day_count = 1
        busiest_day = ""

        for day in self._days_count:
            if self._days_count[day] <= day_count:
                day_count = self._days_count[day]
                busiest_day = day

        return busiest_day


if __name__ == "__main__":
    tacker = TrackOrders()
    tacker.add_new_order("Jafet", "pizza", "segunda-feira")
    tacker.add_new_order("Luis", "Camarao", "quarta-feira")
    tacker.add_new_order("Isabella", "Risito", "terça-feira")
    tacker.add_new_order("Jafet", "pizza", "segunda-feira")
    tacker.add_new_order("Jafet", "hamburguer", "segunda-feira")

    print(tacker.get_least_busy_day())
