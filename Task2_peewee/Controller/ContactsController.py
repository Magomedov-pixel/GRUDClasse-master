from Task2_peewee.Models.Contacts import *

class ContactsController:
    '''
    добавить контакт,
    найти по имени,
    обновить телефон,
    удалить контакт
    '''
    @classmethod
    def add(cls, name, phone, email):
        # добавить студента
        Contacts.create(
            name=name,
            phone=phone,
            email=email,
        )
    @classmethod
    def get_name(cls, name):
        # найти по имени
        return Contacts.select().where(Contacts.name == name)
    @classmethod
    def update_phone(cls, id, new_phone):
        # обновление телефона
        for dict in cls.get():
            if dict['id'] == id:
                dict['phone'] = new_phone
    @classmethod
    def delete(cls, id):
        # удалить контакт
        for dict in cls.get():
            if dict['id'] == id:
                cls.get().remove(dict)

if __name__ == '__main__':
    ContactsController.add(
        'Игорь',
        78955552133,
        "Afghcb@kdspo.po",
    )