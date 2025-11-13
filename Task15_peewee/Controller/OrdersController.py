from Task15_peewee.Model.Orders import *

class OrdersController:
    '''
    создать заказ,
    изменить статус,
    заказы клиента,
    отменить заказ
    '''
    @classmethod
    def add(cls,customer,product,amount,status,order_date):
        # создать заказ
        Orders.create(
            customer=customer,
            product=product,
            amount=amount,
            status=status,
            order_date=order_date
        )
    @classmethod
    def status_update(cls,id,status):
        # изменить статус
        Orders.update({Orders.status:status}).where(Orders.id==id).execute()
    @classmethod
    def get_customer(cls, customer):
        # найти заказы клиента
        return Orders.select().where(Orders.customer == customer)
    @classmethod
    # удалить
    def delite(cls, id):
        Orders.delete_by_id(id)

if __name__ == '__main__':
    OrdersController.add(
        'dkjfgk',
        'sjdk',
        'jdklsjd',
        'skjdik',
        'djfkld'
    )