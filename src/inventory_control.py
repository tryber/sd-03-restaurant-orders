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

        self.inventory = {
            'pao': 0,
            'carne': 0,
            'queijo': 0,
            'molho': 0,
            'presunto': 0,
            'massa': 0,
            'frango': 0,
        }

        self.dishes = set(
            ['hamburguer', 'pizza', 'misto-quente', 'coxinha'])

    def remove_dishes(self, ingredient):
        for dish in self.ingredients:
            ingredients = set(self.ingredients[dish])
            if ingredient in ingredients:
                self.dishes.discard(dish)

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
