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

        self.to_buy = {
            'pao': 0,
            'carne': 0,
            'queijo': 0,
            'molho': 0,
            'presunto': 0,
            'massa': 0,
            'frango': 0,
        }

    def add_new_order(self, costumer, order, day):
        available_dishes = self.get_available_dishes()
        if order not in available_dishes:
            return False
        self.orders.append([costumer, order, day])

        for ingredient in self.ingredients[order]:
            self.to_buy[ingredient] += 1





    def get_quantities_to_buy(self):
        return self.to_buy

    def ingredients_are_available(self, ingredients):        
        for ingredient in ingredients:

            if self.minimum_inventory[ingredient] - self.to_buy[ingredient] <= 0:
                return False
        return True

    def get_available_dishes(self):
        return set([dish for dish in self.ingredients
                if self.ingredients_are_available(self.ingredients[dish])])
