from Task18_peewee.Model.Equipment import *

class EquipmentController:
    '''
    добавить оборудование,
    изменить статус,
    найти по пользователю,
    списать
    '''
    @classmethod
    def add(cls,name,type,serial,status,user):
        # добавить оборудование
        Equipment.create(
            name = name,
            type = type,
            serial = serial,
            status = status,
            user = user
        )
    @classmethod
    def user(cls):
        # изменить статус,
        return Equipment.select().where(Equipment.user == True)
    @classmethod
    def get_genre(cls, user):
        # найти по пользователю
        return Equipment.select().where(Equipment.user == user)
    @classmethod
    def delete(cls, id):
        for dict in cls.get():
            if dict['id'] == id:
                cls.get().remove(dict)
if __name__ == '__main__':
    EquipmentController.add('sdd','ss','sd','sd','sdd')