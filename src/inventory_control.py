class InventoryControl:
    def __init__(self):
        self.orders = dict()
        self.current_expenses = dict(
            {
                "pao": 0,
                "carne": 0,
                "queijo": 0,
                "molho": 0,
                "presunto": 0,
                "massa": 0,
                "frango": 0,
            }
        )
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

    def map_expenses(self, order):
        for ingredient in self.ingredients[order]:
            self.current_expenses[ingredient] += 1

    def add_new_order(self, costumer, order, day):
        if costumer not in self.orders:
            self.orders[costumer] = [order, day]
        else:
            self.orders[costumer].append(order)
            self.orders[costumer].append(day)
        self.map_expenses(order)

    def get_quantities_to_buy(self):
        return self.current_expenses

if __name__ == "__main__":
    test = InventoryControl()
    test.add_new_order("joao", "hamburguer", "sabado")
    test.add_new_order("joao", "hamburguer", "sabado")
    print(test.current_expenses)
