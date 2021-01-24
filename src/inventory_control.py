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
            "carne": 50,
            "queijo": 100,
            "molho": 50,
            "presunto": 50,
            "massa": 50,
            "frango": 50,
        }
        self.inventory = self.minimum_inventory.copy()

        self.orders = []

    def manage_order(self, order):
        recipe = self.ingredients[order]
        order_is_valid = True
        for item in recipe:
            if self.inventory[item] - 1 < 0:
                return False
        if order_is_valid:
            for item in recipe:
                self.inventory[item] -= 1
            return True

    def add_new_order(self, customer, order, day):
        if self.manage_order(order):
            order_dict = {"customer": customer, "item": order, "day": day}
            self.orders.append(order_dict)
        else:
            return False

    def get_quantities_to_buy(self):
        quantities_to_buy = {}
        for item in self.inventory:
            qty = self.minimum_inventory[item] - self.inventory[item]
            quantities_to_buy[item] = qty
        return quantities_to_buy

    def get_available_dishes(self):
        avaliable_dishes = set()
        unavaliable_inventory = set()
        avaliable_inventory = set(self.inventory.keys())
        for item in self.inventory:
            if self.inventory[item] <= 0:
                avaliable_inventory.discard(item)
                unavaliable_inventory.add(item)
        for name, ingredients in self.ingredients.items():
            sliced = set(set(ingredients)).intersection(
                avaliable_inventory
            )
            if sliced == set(ingredients):
                avaliable_dishes.add(name)
        return avaliable_dishes
