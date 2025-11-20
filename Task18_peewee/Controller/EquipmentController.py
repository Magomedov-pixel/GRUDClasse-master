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