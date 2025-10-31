from Task16.Models.Pet import Pet


class PetController:
    '''
    класс для управления моелью Pet
    методы:
        добавить питомца,
        поставить прививку
        вывести список "питомцы владельца",
        найти по типу
    '''
    # CRUD
    obj = Pet()  # создать объект класса  Pet

    @classmethod
    def add(cls, name, type, age, owner, vaccinated=False):
        cls.obj.pets = {
            "name": name,
            "type": type,
            "age": age,
            "owner": owner,
            "vaccinated": vaccinated
        }
        return True

    # прокси метод
    @classmethod
    def get(cls):
        return cls.obj.pets

    # поставить прививку,
    @classmethod
    def vaccinated(cls, id):
        '''
        поменять значение ключа vaccinated  на True по ИД питомца
        в цикле перебрать список с питомца
        :return:
        '''
        for dict in cls.get():
            if dict['id'] == id:
                dict['vaccinated'] = True
                return dict
            else:
                return f'питомца с id {id} нет в базе данных'

    @classmethod
    def list_owner(cls, owner):
        list = []
        for dict in cls.get():
            if dict['owner'] == owner:
                list.append(dict['name'])
        return list

    # найти по типу
    @classmethod
    def type_pet(cls, type):
        result = f"нет {type}"
        for dict in cls.get():
            if dict['type'] == type:
                result = f"есть {type}"
        return result


if __name__ == "__main__":
    print(PetController.get())
    print(PetController.add('Машка', 'кошка', 5, "Мария"))
    print(PetController.get())
    print(PetController.vaccinated(1))
    print(PetController.list_owner('Мария'))
    print(PetController.type_pet('кошка'))
