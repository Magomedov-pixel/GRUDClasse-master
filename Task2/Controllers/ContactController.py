from Task2.Models.Contact import Contact


class ContactController:
    '''
    управляет в классе Contact
    методы:
        добавить,
        показать все,
        обновить телефон,
        удалить
    '''
    obj = Contact()
    # прокси метод вывода всех данных контактов
    @classmethod
    def get(cls):
       return cls.obj.contacts

    #добавить контакт
    @classmethod
    def add(cls,name,phone,email):
        cls.obj.contacts ={"name":name,"phone":phone,"email":email}

    #обновление телефона
    @classmethod
    def update_phone(cls,id,new_phone):
        for dict in cls.get():
            if dict['id'] == id:
                dict['phone'] = new_phone

    # удалить контакт
    @classmethod
    def delete(cls,id):
        for dict in cls.get():
            if dict['id'] == id:
                cls.get().remove(dict)


if __name__=="__main__":

    ContactController.add('vasiliy','79065584236','vasia@gmail.com')
    print(ContactController.get())
    ContactController.update_phone(2,"77777777777")
    print(ContactController.get())
    ContactController.delete(1)
    print(ContactController.get())
