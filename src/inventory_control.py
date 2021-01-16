class InventoryControl:
    def __init__(self):
        self.orders = dict()
        self.available_dishes = {
            "hamburguer",
            "pizza",
            "misto-quente",
            "coxinha",
        }
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
            self.minimum_inventory[ingredient] -= 1

    def get_available_dishes(self):
        for dish in self.ingredients:
            for ingredient in self.ingredients[dish]:
                if (
                    self.minimum_inventory[ingredient] == 0
                    and dish in self.available_dishes
                ):
                    self.available_dishes.remove(dish)
                    break
        return self.available_dishes

    def add_new_order(self, costumer, order, day):
        if order in self.get_available_dishes():
            if costumer not in self.orders:
                self.orders[costumer] = [order, day]
            else:
                self.orders[costumer].append(order)
                self.orders[costumer].append(day)
            self.map_expenses(order)
        else:
            return False

    def get_quantities_to_buy(self):
        return self.current_expenses


if __name__ == "__main__":
    test = InventoryControl()
    test.add_new_order("joao", "hamburguer", "sabado")
    test.add_new_order("joao", "hamburguer", "sabado")
    print(test.current_expenses)
    print(test.get_available_dishes())
    # count = 1
    # while count <= 50:
    #     test.add_new_order("jorge", "coxinha", "terça-feira")
    #     count += 1
    # dishes = test.get_available_dishes()
    # print(dishes)
