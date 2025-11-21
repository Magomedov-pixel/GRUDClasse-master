from Task19_peewee.Model.Workouts import *
class WorkoutsController:
    '''
    добавить тренировку,
    статистика за неделю,
    найти по типу,
    общая продолжительность
    '''
    @classmethod
    def add(cls, date, type, duration, calories, notes):
        # добавить авто
        Workouts.create(
            date=date,
            type=type,
            duration=duration,
            calories=calories,
            notes=notes
        )
    @classmethod
    def type(cls,type):
        # статистика за неделю
        return Workouts.select().where(Workouts.type == type)