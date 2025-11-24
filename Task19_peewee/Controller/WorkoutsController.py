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

    @classmethod
    def type(cls, duration):
        # общая продолжительность
        return Workouts.select().where(Workouts.duration == duration)
if __name__ == "__main__":
    WorkoutsController.type("type")