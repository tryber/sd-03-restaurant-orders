class InventoryControl:
    def __init__(self):
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

        self.inventory = dict.fromkeys(self.minimum_inventory, 0)

        self.dishes = set(self.ingredients.keys())

    def remove_dishes(self, ingredient):
        for recipe in self.ingredients:
            recipe_ingredients = set(self.ingredients[recipe])
            if ingredient in recipe_ingredients:
                self.dishes.discard(recipe)

    def add_new_order(self, costumer, order, day):
        ingredients = self.ingredients[order]
        for ingredient in ingredients:
            if (
                self.inventory[ingredient] + 1 <
                self.minimum_inventory[ingredient]
            ):
                self.inventory[ingredient] += 1
            elif (
                self.inventory[ingredient] + 1 ==
                self.minimum_inventory[ingredient]
            ):
                self.inventory[ingredient] += 1
                self.remove_dishes(ingredient)
            else:
                return False

    def get_quantities_to_buy(self):
        return self.inventory

    def get_available_dishes(self):
        return self.dishes
