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
            "carne": 35,
            "queijo": 100,
            "molho": 30,
            "presunto": 20,
            "massa": 20,
            "frango": 10,
        }
        self.inventory = self.minimum_inventory.copy()

        self.orders = []

    def manage_order(self, order):
        recipe = self.ingredients[order]
        is_valid = True
        for item in recipe:
            if self.inventory[item] - 1 < 0:
                return False
        if is_valid:
            for item in recipe:
                self.inventory[item] -= 1
            return True

    def add_new_order(self, costumer, order, day):
        if self.manage_order(order):
            order_dict = {"person": costumer, "item": order, "day": day}
            self.orders.append(order_dict)
        else:
            return False

    def get_quantities_to_buy(self):
        quantities_to_buy = {}
        for item in self.inventory:
            print(f"{self.minimum_inventory[item]= }")
            print(f"{self.inventory[item]= }")
            difference = self.minimum_inventory[item] - self.inventory[item]
            quantities_to_buy[item] = difference
        return quantities_to_buy

    def get_available_dishes():
        pass