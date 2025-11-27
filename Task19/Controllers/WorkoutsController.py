from Task19.Models.Workouts import Workouts
class WorkoutsController:
    '''
    добавить тренировку,
    статистика за неделю,
    найти по типу,
    общая продолжительность
    '''
    obj = Workouts()
    @classmethod
    def get(cls):
        return cls.obj.workouts
    @classmethod
    def add(cls,date, type, duration, calories, notes):
        cls.obj.workouts = {"date":date,"type":type,"duration":duration,"calories":calories,"notes":notes}
    @classmethod
    def type(cls, type):
        result = f"нет {type}"
        for dict in cls.get():
            if dict['type'] == type:
                result = f"есть {type}"
        return result

if __name__ == '__main__':
    print(WorkoutsController.get())