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
        if order not in self.get_available_dishes():
            return False

        ingredients = self.ingredients[order]

        for ingredient in ingredients:
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

    def get_available_dishes(self):
        ingredients = set(self.orders_used_inventory.keys())
        meals = set(self.ingredients.keys())
        meal_to_remove = set()
        for ingredient in ingredients:
            if self.orders_used_inventory[ingredient] == 0:
                for meal in meals:
                    if ingredient in self.ingredients[meal]:
                        meal_to_remove.add(meal)
        return meals.difference(meal_to_remove)


if __name__ == "__main__":
    inventory = InventoryControl()
    for i in range(50):
        print(inventory.add_new_order("jorge", "pizza", "terça-feira"))

    # print(inventory.get_available_dishes())
