from src.analyze_log import get_most_ordered_dish_per_costumer as get_most_ord
from src.analyze_log import create_order_base, save_dishes, save_date
from src.analyze_log import get_never_ord, get_never_visited


class TrackOrders:
    def __init__(self):
        self._tracks = dict()
        self._dishes = set()
        self._work_days = set()

    def __len__(self):
        return len(self._tracks)

    def add_new_order(self, costumer, order, day):
        self._dishes.add(order)
        self._work_days.add(day)
        row = [costumer, order, day]
        create_order_base(row, self._tracks)
        save_date(row, self._tracks)
        save_dishes(row, self._tracks)

    def get_most_ordered_dish_per_costumer(self, costumer):
        return get_most_ord(self._tracks, costumer)

    def get_order_frequency_per_costumer(self, costumer, order):
        pass

    def get_never_ordered_per_costumer(self, costumer):
        return get_never_ord(self._dishes, costumer, self._tracks)

    def get_days_never_visited_per_costumer(self, costumer):
        return get_never_visited(self._work_days, costumer, self._tracks)

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
