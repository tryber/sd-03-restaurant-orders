class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        qnt_by_recipe = {}
        for name, recipe, day in self.orders:
            if name == costumer:
                qnt_by_recipe[recipe] = qnt_by_recipe.get(recipe, 0) + 1

        return max(qnt_by_recipe, key=qnt_by_recipe.get)

    def get_order_frequency_per_costumer(self, costumer, order):
        qnt_by_rec_by_clt = {}
        for customer, recipe in self.orders:
            if customer not in qnt_by_rec_by_clt:
                qnt_by_rec_by_clt[customer] = {recipe: 1}
                continue
            qnt_by_rec_by_clt[customer][recipe] = (
                qnt_by_rec_by_clt[customer].get(recipe, 0) + 1
            )

        return qnt_by_rec_by_clt

    def get_never_ordered_per_costumer(self, costumer):
        all_recipes = set()
        ordered_recipes = set()

        for name, recipe, day in self.orders:
            all_recipes.add(recipe)
            if name == costumer:
                ordered_recipes.add(recipe)

        return all_recipes.difference(ordered_recipes)

    def get_days_never_visited_per_costumer(self, costumer):
        all_days = set()
        visited_days = set()

        for name, _, day in self.orders:
            all_days.add(day)
            if name == costumer:
                visited_days.add(day)

        return all_days.difference(visited_days)

    def get_busiest_day(self):
        orders_qnt_by_day = {}
        for _, _, day in self.orders:
            orders_qnt_by_day[day] = orders_qnt_by_day.get(day, 0) + 1

        return max(orders_qnt_by_day, key=orders_qnt_by_day.get)

    def get_least_busy_day(self):
        orders_qnt_by_day = {}
        for _, _, day in self.orders:
            orders_qnt_by_day[day] = orders_qnt_by_day.get(day, 0) + 1

        return min(orders_qnt_by_day, key=orders_qnt_by_day.get)


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

    track_orders = TrackOrders()
    for name, food, day in csv_parsed:
        track_orders.add_new_order(name, food, day)
    never_visited = track_orders.get_days_never_visited_per_costumer("joao")
