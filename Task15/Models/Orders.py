class Order:
    def __init__(self):
        self.__list_orders = [
            {"id": 1, "customer": "Иван", "product": "Ноутбук", "amount": 1, "status":"доставляется", "order_date": "2024-01-20"}
        ]
        self.id = 2
    @property
    def orders(self):
        return self.__list_orders

    @orders.setter
    def orders(self, dict):
        dict['id'] = self.id
        self.orders.append(dict)
        self.id += 1
if __name__ == '__main__':
    ord = Order()
    print(ord.orders)