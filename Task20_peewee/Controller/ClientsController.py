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
    @classmethod
    def status(cls):
        # отметить пройденной
        return Clients.select().where(Clients.status == False)
    @classmethod
    def get_name(cls, name):
        # найти по названию,
        return Clients.select().where(Clients.name == name)
if __name__ == "__main__":
    ClientsController.add("sds",'sd','sd','sdd','sddd')