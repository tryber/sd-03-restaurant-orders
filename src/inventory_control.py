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

        self.orders = []

        self.inventory = {
            'pao': 50,
            'carne': 50,
            'queijo': 100,
            'molho': 50,
            'presunto': 50,
            'massa': 50,
            'frango': 50,
        }

    def add_new_order(self, _customer, order, _day):
        ingredients = self.ingredients[order]
        for ingredient in ingredients:
            if self.inventory[ingredient] > 0:
                self.inventory[ingredient] -= 1
            else:
                return False

    def get_quantities_to_buy(self):
        buy_list = {}
        ingredient_list = set(self.inventory.keys())
        original = self.minimum_inventory
        current = self.inventory
        for ingredient in ingredient_list:
            buy_list[ingredient] = original[ingredient] - current[ingredient]
        return buy_list

    def get_available_dishes(self):
        ingredient_list = set(self.inventory.keys())
        restaurant_food = set(self.ingredients.keys())
        unavailable_food = set()
        for ingredient in ingredient_list:
            if self.inventory[ingredient] <= 0:
                for food in restaurant_food:
                    if ingredient in self.ingredients[food]:
                        unavailable_food.add(food)
        return restaurant_food.difference(unavailable_food)
