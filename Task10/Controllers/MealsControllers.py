from Task10.Models.Meals import Meals


class MealsController:
    '''
     добавить прием пищи,
     калории за день,
     найти по времени
    '''
    obj = Meals()

    @classmethod
    def get(cls):
        return cls.obj.meals
    # добавить прием пищи
    @classmethod
    def add(cls,meal,food,calories,time):
        cls.obj.meals = {"meal":meal,"food":food,"calories":calories,"time":time}
    # найти
    @classmethod
    def t_time(cls, time):
        result = f"нет {time}"
        for dict in cls.get():
            if dict['time'] == time:
                result = f"есть {time}"
        return result

if __name__ == '__main__':
    print(MealsController.get())

