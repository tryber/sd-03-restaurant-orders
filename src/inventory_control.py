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

        self.inventory = {
            "pao": 50,
            "carne": 35,
            "queijo": 100,
            "molho": 30,
            "presunto": 20,
            "massa": 20,
            "frango": 10,
        }

    def add_new_order(self, costumer, order, day):
        for ingredient in self.ingredients[order]:
            self.inventory[ingredient] -= 1

    def get_shopping_list(self):
        return {
            ingredient: self.minimum_inventory[ingredient] - qnt
            for ingredient, qnt in self.inventory.items()
        }

    def get_available_dishes(self):
        available_dishes = []
        for recipe, ingredients in self.ingredients.items():
            available_dishes.append(recipe)
            for ingredient in ingredients:
                if self.inventory[ingredient] == 0:
                    available_dishes.pop()

        return available_dishes


if __name__ == "__main__":
    inventory = InventoryControl()
    inventory.add_new_order("jorge", "hamburguer", "terça-feira")
    inventory.add_new_order("jorge", "hamburguer", "terça-feira")
    hamburguer = inventory.get_shopping_list()
    total_ingredients = {
        "pao": 2,
        "carne": 2,
        "queijo": 2,
        "molho": 0,
        "presunto": 0,
        "massa": 0,
        "frango": 0,
    }
    print(hamburguer)
