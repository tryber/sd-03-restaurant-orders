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

        self.orders_used_inventory = self.minimum_inventory.copy()

    def add_new_order(self, costumer, order, day):
        ingredients = self.ingredients[order]
        for ingredient in ingredients:
            # if ingredient not in self.orders_used_inventory:
            #     self.orders_used_inventory[ingredient] = 1
            # else:
            self.orders_used_inventory[ingredient] -= 1

    def get_quantities_to_buy(self):
        what_to_buy = {}
        for ingredient in self.orders_used_inventory:
            quantity_to_buy = (
                self.minimum_inventory[ingredient]
                - self.orders_used_inventory[ingredient]
            )
            what_to_buy[ingredient] = quantity_to_buy
        return what_to_buy


if __name__ == "__main__":
    inventory = InventoryControl()
    inventory.add_new_order("jorge", "pizza", "terça-feira")
    print(inventory.get_quantities_to_buy())
