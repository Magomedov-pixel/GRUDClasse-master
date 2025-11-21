from Task20_peewee.Model.Clients import *

class ClientsController:
    '''
    добавить клиента,
    изменить статус,
    найти по названию,
    контакты клиента
    '''
    @classmethod
    def add(cls,name,contact_person,phone,email,status):
        # добавить игру
        Clients.create(
            name = name,
            contact_person = contact_person,
            phone = phone,
            email = email,
            status = status
        )

