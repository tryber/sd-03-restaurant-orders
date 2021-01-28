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

    # removendo item do cardapio se ingredientes indisponiveis
    def remove_unavailable_dishes(self, ingredient):
        for recipe in self.ingredients:
            recipe_ingredients = set(self.ingredients[recipe])
            if ingredient in recipe_ingredients:
                # usando metodo discard para não subir erro em caso de
                # inexistência do item no cardápio
                self.dishes.discard(recipe)

    def add_new_order(self, costumer, order, day):
        order_ingredients = self.ingredients[order]
        # comparando quantidades futuras com limite de estoque minimo
        for ingredient in order_ingredients:
            if (
                self.quantities_to_buy[ingredient] + 1
                > self.minimum_inventory[ingredient]
            ):
                return False
            elif (
                self.quantities_to_buy[ingredient] + 1
                == self.minimum_inventory[ingredient]
            ):
                self.quantities_to_buy[ingredient] += 1
                self.remove_unavailable_dishes(ingredient)
            else:
                self.quantities_to_buy[ingredient] += 1

    def get_quantities_to_buy(self):
        return self.quantities_to_buy

    def get_available_dishes(self):
        return self.dishes
