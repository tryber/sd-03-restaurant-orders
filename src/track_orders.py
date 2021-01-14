class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def extract_food_from_orders_by_person(self):
        orders_by_food = {}
        for person, food, day in self.orders:
            if person not in orders_by_food:
                orders_by_food[person] = [food]
            else:
                orders_by_food[person].append(food)
        return orders_by_food

    def extract_day_from_orders_by_person(self):
        orders_by_day = {}
        for person, food, day in self.orders:
            if person not in orders_by_day:
                orders_by_day[person] = [day]
            else:
                orders_by_day[person].append(day)
        return orders_by_day

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        foods_dict = {}
        foods_from_person = self.extract_food_from_orders_by_person()
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
        all_foods = set()
        foods_from_person = self.extract_food_from_orders_by_person()
        print(foods_from_person)
        for person in foods_from_person:
            for food in foods_from_person[person]:
                all_foods.add(food)
        return all_foods.difference(foods_from_person[costumer])

    def get_order_frequency_per_costumer(self, costumer, order):
        pass

    def get_days_never_visited_per_costumer(self, costumer):
        days_from_person = self.extract_day_from_orders_by_person()
        return days_from_person

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass


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
        ["joao", "hamburguer", "terça-feira"]
    ]
    trackOrders = TrackOrders()
    for name, food, day in csv_parsed:
        trackOrders.add_new_order(name, food, day)
    # print(trackOrders.get_most_ordered_dish_per_costumer("maria"))
    # print(trackOrders.get_never_ordered_per_costumer("maria"))
    print(trackOrders.get_days_never_visited_per_costumer("maria"))
