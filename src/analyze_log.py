import csv


class Analyze_log:
    @staticmethod
    def import_csv(path):
        data = []
        with open(path) as file:
            reader = csv.reader(file)
            for person, item, day in reader:
                order_dict = {"person": person, "item": item, "day": day}
                data.append(order_dict)
        return data

    def __init__(self, path):
        self.orders = self.import_csv(path)

    def most_ordered(self, client):
        most_ordered = ""
        counter = {}
        for order in self.orders:
            item = order["item"]
            if order["person"] == client:
                if counter.get(order["item"], 0):
                    counter[item] += 1
                else:
                    counter[item] = 1
            if most_ordered == "" or counter.get(item, 0) > counter.get(
                most_ordered, 0
            ):
                most_ordered = item
        return most_ordered

    def times_ordered_by_client(self, item, client):
        counter = 0
        for order in self.orders:
            if order["person"] == client and order["item"] == item:
                counter += 1
        return counter

    def item_never_ordered_by_client(self, client):
        menu = set()
        ordered_by_client = set()
        for order in self.orders:
            menu.add(order["item"])
            if order["person"] == client:
                ordered_by_client.add(order["item"])
        difference = menu.difference(ordered_by_client)
        return difference

    def days_client_never_went(self, client):
        days = set()
        days_went = set()
        for order in self.orders:
            days.add(order["day"])
            if order["person"] == client:
                days_went.add(order["day"])
        difference = days.difference(days_went)
        return difference


def analyze_log(path_to_file):
    logger = Analyze_log(path_to_file)
    logs = [
        logger.most_ordered("maria"),
        logger.times_ordered_by_client("hamburguer", "arnaldo"),
        logger.item_never_ordered_by_client("joao"),
        logger.days_client_never_went("joao"),
    ]
    with open("data/mkt_campaign.txt", "w") as file:
        for log in logs:
            file.writelines(f"{log}\n")


if __name__ == "__main__":
    analyze_log("data/orders_1.csv")
