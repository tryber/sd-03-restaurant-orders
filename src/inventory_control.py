class InventoryControl:
    def __init__(self):
        self.orders = []

        self.ingredients = {
            'hamburguer': ['pao', 'carne', 'queijo'],
            'pizza': ['massa', 'queijo', 'molho'],
            'misto-quente': ['pao', 'queijo', 'presunto'],
            'coxinha': ['massa', 'frango'],
        }

        self.minimum_inventory = {
            'pao': 50,
            'carne': 50,
            'queijo': 100,
            'molho': 50,
            'presunto': 50,
            'massa': 50,
            'frango': 50,
        }

        self.demand = {
            'pao': 0,
            'carne': 0,
            'queijo': 0,
            'molho': 0,
            'presunto': 0,
            'massa': 0,
            'frango': 0,
        }

    def add_new_order(self, customer, order, day):
        self.orders.append([(customer, order, day), "Unchecked"])
        available_dishes = self.get_available_dishes()
        if not available_dishes:
            self.orders.pop()
            return False
        self.get_quantities_to_buy()
        self.orders[len(self.orders) - 1][1] = "Checked"

    def get_quantities_to_buy(self):
        for order_item in self.orders:
            _, dish, _ = order_item[0]
            ingredients = self.ingredients[dish]
            for ingredient in ingredients:
                if order_item[1] == "Unchecked":
                    self.demand[ingredient] += 1
                    self.minimum_inventory[ingredient] -= 1
        return self.demand

    def get_available_dishes(self):
        dishes = set([*self.ingredients.keys()])
        avail_dishes = set()
        avail_ingredients = set()

        for ingredient in [*self.minimum_inventory.keys()]:
            if self.minimum_inventory[ingredient] > 0:
                avail_ingredients.add(ingredient)

        for dish in dishes:
            ingredients = set(self.ingredients[dish])
            if len(ingredients) == len(
                ingredients.intersection(avail_ingredients)
            ):
                avail_dishes.add(dish)

        return avail_dishes
