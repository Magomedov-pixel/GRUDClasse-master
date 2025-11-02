from Task15.Models.Orders import Order
class OrderController:
    '''изменить статус, заказы клиента, отменить заказ'''
    obj = Order()
    @classmethod
    def get(cls):
        return cls.obj.orders
    @classmethod
    def update_status(cls,id,new_status):
        for dict in cls.get():
            if dict['id'] == id:
                dict['status'] = new_status
    @classmethod
    def customers(cls, customer):
        result = f"нет {customer}"
        for dict in cls.get():
            if dict['customer'] == customer:
                result = f"есть {customer}"
        return result
    @classmethod
    def delete(cls, id):
        for dict in cls.get():
            if dict['id'] == id:
                cls.get().remove(dict)
if __name__ == '__main__':
    print(OrderController.get())
