class InventoryControl:
    def __init__(self):
        self.ingredients = {
            "hamburguer": ["pao", "carne", "queijo"],
            "pizza": ["massa", "queijo", "molho"],
            "misto-quente": ["pao", "queijo", "presunto"],
            "coxinha": ["massa", "frango"],
        }

        self.minimum_inventory = {
            "pao": 50,
            "carne": 35,
            "queijo": 100,
            "massa": 20,
            "molho": 30,
            "tomate": 35,
            "presunto": 20,
            "frango": 10,
        }
        self.orders = []

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])
        self.order = order
        return self.get_available_dishes()

    def returning(self):
        for order in self.orders:
            for ing in self.ingredients[order[1]]:
                self.foods[ing] += 1
        return self.foods

    def get_quantities_to_buy(self):
        self.foods = {}
        self.ingredientss = set()
        for food, ing in self.ingredients.items():
            for i in ing:
                self.ingredientss.add(i)
        for i in self.ingredientss:
            self.foods[i] = 0
        return self.returning()

    def get_set_of_foods(self):
        foods = set()
        for food in self.ingredients:
            foods.add(food)
        return foods

    def get_set_of_unavailable(self):
        unavailable = set()
        for ing in self.ingredients[self.order]:
            self.minimum_inventory[ing] = self.minimum_inventory[ing] - 1
        for food, ingredients in self.ingredients.items():
            for ingredient in ingredients:
                if self.minimum_inventory[ingredient] == 0:
                    unavailable.add(food)
        return unavailable

    def get_available_dishes(self):
        for ing, qty in self.minimum_inventory.items():
            if qty == 0:
                return False
        foods = self.get_set_of_foods()
        unavailable = self.get_set_of_unavailable()

        return foods.difference(unavailable)
