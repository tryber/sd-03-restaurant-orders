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

        # inicializando lista de compras a partir do inventário mínimo
        self.quantities_to_buy = dict.fromkeys(self.minimum_inventory, 0)

        # inicializando cardapio a partir de registro de receitas
        self.dishes = set(self.ingredients.keys())

    def add_new_order(self, costumer, order, day):
        order_ingredients = self.ingredients[order]
        for ingredient in order_ingredients:
            if (
                self.quantities_to_buy[ingredient]
                >= self.minimum_inventory[ingredient]
            ):
                return False
            self.quantities_to_buy[ingredient] += 1

    def get_quantities_to_buy(self):
        return self.quantities_to_buy

    def get_available_dishes(self):
        return self.dishes
