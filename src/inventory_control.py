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
        self.get_available_dishes()

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

    def get_available_dishes(self):
        pass

    # ingredients = set(self.orders_used_inventory.keys())
    # meals = set(self.ingredients.keys())
    # meal_to_remove = set()
    # for ingredient in ingredients:
    #     if self.orders_used_inventory[ingredient] == 0:
    #         for meal in meals:
    #             if ingredient in self.ingredients[meal]:
    #                 meal_to_remove.add(meal)
    # return meals.difference(meal_to_remove)
