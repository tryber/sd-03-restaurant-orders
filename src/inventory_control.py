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
            'pao': 50,
            'carne': 50,
            'queijo': 100,
            'molho': 50,
            'presunto': 50,
            'massa': 50,
            'frango': 50,
        }

        self.ingredients_to_buy = {}

        self.order_ingredients = list()

    def add_new_order(self, costumer, order, day):
        self.order_ingredients = self.ingredients[order]
        for ingredient in self.order_ingredients:
            if self.inventory[ingredient] <= 0:
                return False
            self.inventory[ingredient] -= 1

    def get_quantities_to_buy(self):
        for ingredient, qty in self.inventory.items():
            self.ingredients_to_buy[ingredient] = (
                self.minimum_inventory[ingredient] - self.inventory[ingredient]
            )
        return self.ingredients_to_buy
