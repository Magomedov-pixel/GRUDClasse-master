from Task10_peewee.Model.Meals import *

class MealsController:
    '''
    добавить прием пищи,
    калории за день,
    найти по времени
    '''

    @classmethod
    def add(cls, meal, food, calories, time):
        # добавить прием пищи,
        Meals.create(
            meal=meal,
            food=food,
            calories=calories,
            time=time
        )
    @classmethod
    def year(cls, calories):
        # калории за день,
        return Meals.select().where(Meals.calories == calories)

    @classmethod
    def year(cls, time):
        #  найти по времени,
        return Meals.select().where(Meals.time == time)