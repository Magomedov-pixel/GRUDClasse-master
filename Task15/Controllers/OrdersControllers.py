from Task15.Models.Orders import Order
class OrderController:
    obj = Order()
    @classmethod
    def get(cls):
        return cls.obj.orders
