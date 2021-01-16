class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def extract_data_by_person(self, index):
        orders_dict = {}
        for data in self.orders:
            if data[0] not in orders_dict:
                orders_dict[data[0]] = [data[index]]
            else:
                orders_dict[data[0]].append(data[index])
        return orders_dict

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        foods_dict = {}
        foods_from_person = self.extract_data_by_person(1)
        most_ordered = foods_from_person[costumer][0]
        for food in foods_from_person[costumer]:
            if food not in foods_dict:
                foods_dict[food] = 1
            else:
                foods_dict[food] += 1
            if foods_dict[most_ordered] < foods_dict[food]:
                most_ordered = food
        return most_ordered

    def get_never_ordered_per_costumer(self, costumer):
        all_data = set()
        foods_from_person = self.extract_data_by_person(1)
        for person in foods_from_person:
            for food in foods_from_person[person]:
                all_data.add(food)
        return all_data.difference(foods_from_person[costumer])

    def get_days_never_visited_per_costumer(self, costumer):
        all_days = set()
        days_from_person = self.extract_data_by_person(2)
        for person in days_from_person:
            for day in days_from_person[person]:
                all_days.add(day)
        return all_days.difference(days_from_person[costumer])

    def get_busiest_day(self):
        all_days_counter = {}
        days_from_person = self.extract_data_by_person(2)
        busiest = ''
        flag = True
        for person in days_from_person:
            for day in days_from_person[person]:
                if day not in all_days_counter:
                    all_days_counter[day] = 1
                else:
                    all_days_counter[day] += 1
                if flag or all_days_counter[busiest] < all_days_counter[day]:
                    busiest = day
                    flag = False
        return busiest

    def get_least_busy_day(self):
        all_days_counter = {}
        days_from_person = self.extract_data_by_person(2)
        busiest = ''
        flag = True
        for person in days_from_person:
            for day in days_from_person[person]:
                if day not in all_days_counter:
                    all_days_counter[day] = 1
                else:
                    all_days_counter[day] += 1
                if flag or all_days_counter[busiest] > all_days_counter[day]:
                    busiest = day
                    flag = False
        return busiest


if __name__ == "__main__":
    csv_parsed = [
        ["maria", "pizza", "terça-feira"],
        ["maria", "hamburguer", "terça-feira"],
        ["joao", "hamburguer", "terça-feira"],
        ["maria", "coxinha", "segunda-feira"],
        ["arnaldo", "misto-quente", "terça-feira"],
        ["jose", "hamburguer", "sabado"],
        ["maria", "hamburguer", "terça-feira"],
        ["maria", "hamburguer", "terça-feira"],
        ["joao", "hamburguer", "terça-feira"],
    ]
    trackOrders = TrackOrders()
    for name, food, day in csv_parsed:
        trackOrders.add_new_order(name, food, day)
    print(trackOrders.get_most_ordered_dish_per_costumer("maria"))
    print(trackOrders.get_never_ordered_per_costumer("maria"))
    print(trackOrders.get_order_frequency_per_costumer("joao"))
    print(trackOrders.get_busiest_day())
    print(trackOrders.get_least_busy_day())
