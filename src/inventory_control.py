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

    def add_new_order(self, costumer, order, day):
        pass

    def get_quantities_to_buy(self):
        return self.inventory

    def get_available_dishes(self):
        return self.dishes
