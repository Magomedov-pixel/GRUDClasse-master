from Task14_peewee.Model.Cars import *


class CarsController:
    '''
    добавить авто,
    найти по марке,
    авто определенного года,
    изменить цену
    '''

    @classmethod
    def add(cls, brand, model, year, color, price):
        # добавить авто
        Cars.create(brand=brand, model=model, year=year, color=color, price=price)

    @classmethod
    def get_Cars(cls, brand):
        # найти по марке
        return Cars.select().where(Cars.brand == brand)

    @classmethod
    def year(cls, year):
        # авто определенного года
        return Cars.select().where(Cars.year == year)

    @classmethod
    def grade_update(cls, id, price):
        # изменить цену
        Cars.update({Cars.price: price}).where(Cars.id == id).execute()


if __name__ == '__main__':
    CarsController.add(
        'mersedes',
        'gt63s',
        2025,
        'black',
        20000000
    )
