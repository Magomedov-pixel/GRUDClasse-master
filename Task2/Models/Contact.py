class Contact:
    '''
    класс для контактов в телефоне {"id": 1, "name": "Иван", "phone": "+79123456789", "email":"ivan@mail.ru"}
    класс хранит список словарей {"id": 1, "name": "Иван", "phone": "+79123456789", "email":"ivan@mail.ru"}
    '''

    def __init__(self):
        self.__list_contacts = [
            {
                "id": 1,
                "name": "Иван",
                "phone": "+79123456789",
                "email": "ivan@mail.ru"}
        ]
        self.id = 2

    # создаем гетер который выводит список контактов
    @property
    def contacts(self):
        '''

        :return:
            возвращяет список словарей
        '''
        return self.__list_contacts
    # сетер метод который добавит список словарь с контактом
    @contacts.setter
    def contacts(self,dict):
        dict['id'] = self.id# присвоить ключу id в словаре значение атрибута self.id
        self.contacts.append(dict) # через геттер contacts получаем список словарей и добавляем новый словарь
        self.id += 1 # увеличить на 1


if __name__ == '__main__':
   con = Contact()
   print(con.contacts)
   con.contacts = {"name":"Света"}
   print((con.contacts))