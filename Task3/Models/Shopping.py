class Shopping:
    def __init__(self):
        self.__list_shopping = [
            {"id": 1, "product": "Хлеб", "quantity": 1, "bought": False},
            {"id": 2, "product": "Молоко", "quantity": 2, "bought": True}
        ]
        self.id = 3
    @property
    def shoppings(self):
        return self.__list_shopping

    @shoppings.setter
    def shoppings(self, dict):
        dict['id'] = self.id
        self.shoppings.append(dict)
        self.id += 1

if __name__ == '__main__':
    shop = Shopping()
    print(shop.shoppings)
    shop.shoppings = {"product":"бананы", "quantity":2}
    print(shop.shoppings)