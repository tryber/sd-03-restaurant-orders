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

        self.stock = {
            'pao': 50,
            'carne': 50,
            'queijo': 100,
            'molho': 50,
            'presunto': 50,
            'massa': 50,
            'frango': 50,
        }
        self.dishes_asked = []

    def add_new_order(self, _customer, order, _day):
        ingredients = self.ingredients[order]
        print(ingredients)
        for ingredient in ingredients:
            if self.stock[ingredient] > 0:
                self.stock[ingredient] -= 1
            else:
                return None

    def get_quantities_to_buy(self):
        needed_in = {}
        ingredient_list = set(self.stock.keys())
        stock_bf = self.minimum_inventory
        stock_af = self.stock
        for ingredient in ingredient_list:
            needed_in[ingredient] = stock_bf[ingredient] - stock_af[ingredient]
        return needed_in
