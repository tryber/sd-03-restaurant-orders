from src.analyze_log import top_order
from src.analyze_log import format_data, save_dishes, save_date
from src.analyze_log import get_never_ordered_per_costumer
from src.analyze_log import get_days_never_visited_per_costumer


class TrackOrders:
    def __init__(self):
        self._tracks = dict()
        self._dishes = set()
        self._work_days = set()
        self._busy_days = dict()

    def __len__(self):
        return len(self._tracks)

    def busy_days(self, day):
        if day not in self._busy_days:
            self._busy_days[day] = 1
        else:
            self._busy_days[day] += 1

    def add_new_order(self, costumer, order, day):
        self.busy_days(day)
        self._dishes.add(order)
        self._work_days.add(day)
        row = [costumer, order, day]
        format_data(row, self._tracks)
        save_date(row, self._tracks)
        save_dishes(row, self._tracks)

    def get_most_ordered_dish_per_costumer(self, costumer):
        return top_order(self._tracks, costumer)

    def get_order_frequency_per_costumer(self, costumer, order):
        pass

    def get_get_never_ordered_per_costumer(self, costumer):
        return get_never_ordered_per_costumer(self._dishes, costumer, self._tracks)

    def get_days_get_days_never_visited_per_costumer(self, costumer):
        return get_days_never_visited_per_costumer(
            self._work_days, costumer, self._tracks)

    def get_busiest_day(self):
        return max(self._busy_days, key=self._busy_days.get)

    def get_least_busy_day(self):
        return min(self._busy_days, key=self._busy_days.get)
