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

    def add_new_order(self, customer, order, day):
        self.orders.append((customer, order, day))
        self.get_quantities_to_buy()

    def get_quantities_to_buy(self):
        demand = {
            'pao': 0,
            'carne': 0,
            'queijo': 0,
            'molho': 0,
            'presunto': 0,
            'massa': 0,
            'frango': 0,
        }

        for _, order, _ in self.orders:
            ingredients = self.ingredients[order]
            for item in ingredients:
                demand[item] += 1

        return demand
