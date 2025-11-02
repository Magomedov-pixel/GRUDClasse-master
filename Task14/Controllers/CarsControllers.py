from Task14.Models.Cars import Car
class CarsController:
    '''
    добавить авто,
    найти по марке,
    авто определенного года,
    изменить цену
    '''
    obj = Car()
    @classmethod
    def get(cls):
        return cls.obj.cars
    @classmethod
    def add(cls,brand, model, year, color, price):
        cls.obj.cars = {"brand":brand,"model":model,"year":year,"color":color,"price":price}
    @classmethod
    def brand(cls, brand):
        result = f"нет {brand}"
        for dict in cls.get():
            if dict['brand'] == brand:
                result = f"есть {brand}"
        return result
    @classmethod
    def year(cls, year):
        result = f"нет {year}"
        for dict in cls.get():
            if dict['year'] == year:
                result = f"есть {year}"
        return result
    @classmethod
    def update_price(cls, id, update_price):
        for dict in cls.get():
            if dict['id'] == id:
                dict['price'] = update_price
if __name__ == '__main__':
    print(CarsController.get())