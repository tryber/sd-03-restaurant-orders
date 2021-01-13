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

        self.inventory = {
            "pao": 50,
            "carne": 50,
            "queijo": 100,
            "molho": 50,
            "presunto": 50,
            "massa": 50,
            "frango": 50,
        }

    def add_new_order(self, costumer, order, day):
        ingrs = []
        for ingredient in self.ingredients[order]:
            if self.inventory[ingredient] <= 0:
                return False
            ingrs.append(ingredient)
        for ingr in ingrs:
            self.inventory[ingr] -= 1

    def get_quantities_to_buy(self):
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
                    break

        return available_dishes


if __name__ == "__main__":
    ingredients = InventoryControl()
    count = 1
    while count <= 50:
        ingredients.add_new_order("jorge", "coxinha", "terça-feira")
        count += 1
    dishes = ingredients.get_available_dishes()
    print(dishes)