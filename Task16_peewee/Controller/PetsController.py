from Task16_peewee.Model.Pets import *
class PetsController:
    '''
    добавить питомца,
    отметить прививку,
    питомцы владельца,
    найти по типу
    '''
    @classmethod
    def add(cls,name,type,age,owner,vaccinated):
        # добавить питомца
        Pets.create(
            name = name,
            type = type,
            age = age,
            owner = owner,
            vaccinated = vaccinated
        )
    @classmethod
    def vaccinated(cls, id):
        # отметить прививку
        for dict in cls.get():
            if dict['id'] == id:
                dict['vaccinated'] = True
                return dict
    @classmethod
    def get_Cars(cls, owner):
        # питомцы владельца
        return Pets.select().where(Pets.owner == owner)
    @classmethod
    def type_pet(cls, type):
        result = f'Нет - {type}'
        for dict in cls.get():
            if dict['type'] == type:
                result = f'Есть {type}'
        return result
if __name__ == '__main__':
    PetsController.add('petr','ket', 3, 'viktor',True)