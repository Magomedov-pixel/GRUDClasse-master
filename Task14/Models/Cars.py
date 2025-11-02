class Car:
    def __init__(self):
        self.__list_cars = [
            {"id": 1, "brand": "Toyota", "model": "Camry", "year": 2020, "color":"черный", "price": 2000000}
        ]
        self.id = 2
    @property
    def cars(self):
        return self.__list_cars
    @cars.setter
    def cars(self, dict):
        dict['id'] = self.id
        self.cars.append(dict)
        self.id += 1

if __name__ == '__main__':
    car = Car()
    print(car.cars)
