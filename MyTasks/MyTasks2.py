class MyTasks2:
    '''
    Система для хранения контактов
    '''

    def __init__(self):
        '''
        создание контактов и их хранение
        '''
        self.__contacts = [
            {"id": 1, "name": "Иван", "phone": "+79123456789", "email":"ivan@mail.ru"}
        ]
        self.id = 2 # автоматическое квеличение класса id

    def add(self,contact):
        self.contacts.append(
            {
                "id": self.id,
                "name": "Иван",
                "contact": contact,
                "email": "ivan@mail.ru"
            }
        )
        self.id += 1
        return True

    @property
    def contacts(self):
        return self.__contacts
    def completed(self,id):
        for dict in self.__contacts:
            if dict['id'] == id:
                dict['completed'] = True
                return dict

    def delete(self,id):
        for dict in self.__contacts:
            if dict['id'] == id:
                self.__contacts.remove(dict)

if __name__ == "__main__":
    contact = MyTasks2()
    print(contact.contacts)
    contact.add("6789779988788998978")
    print(contact.contacts)
    contact.add("7777777777")
    print(contact.contacts)
    contact.delete(1)
    print(contact.contacts)