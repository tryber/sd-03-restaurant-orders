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

        self.inventory = {
            'pao': 50,
            'carne': 50,
            'queijo': 100,
            'molho': 50,
            'presunto': 50,
            'massa': 50,
            'frango': 50,
        }

    def add_new_order(self, customer, order, day):
        self.orders.append([(customer, order, day), "Unchecked"])
        self.get_quantities_to_buy()
        available_dishes = self.get_available_dishes()
        self.orders[len(self.orders) - 1][1] = "Checked"
        if not available_dishes:
            return False


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

        order_is_possible = True

        for order_item in self.orders:
            _, dish, _ = order_item[0]
            if order_item[1] == "Unchecked":
                ingredients = self.ingredients[dish]
                for ingredient in ingredients:
                    demand[ingredient] += 1
                    self.inventory[ingredient] -= 1
        return demand

    def get_available_dishes(self):
        dishes = set([*self.ingredients.keys()])
        avail_dishes = set([*self.ingredients.keys()])

        order_is_possible = True

        for dish in dishes:
            ingredients = self.ingredients[dish]
            for ingredient in ingredients:
                print(f'Ingrediente: {ingredient}, prato: {dish}, qtd ingrediente: {self.inventory[ingredient]}')
                if self.inventory[ingredient] < 0:
                    order_is_possible = False
                    if dish in avail_dishes:
                        avail_dishes.remove(dish)
                elif self.inventory[ingredient] == 0:
                    if dish in avail_dishes:
                        avail_dishes.remove(dish)

        if not order_is_possible:
            return False
        return avail_dishes




