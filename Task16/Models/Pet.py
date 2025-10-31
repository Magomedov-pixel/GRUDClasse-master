class Pet:
    """
    класс для описания питомцев в ветеринарной клинике
    методы:
    добавить питомца,
    отметить прививку,
    питомцы владельца,
    найти по типу
    """

    def __init__(self):
        self.__list_pets = [
            {"id": 1, "name": "Барсик", "type": "кот", "age": 3, "owner": "Мария", "vaccinated": True}
        ] #список питомцев
        self.id =2

    @property
    def pets(self):
        '''

        :return:
            список питомуев
        '''
        return self.__list_pets
    @pets.setter
    def pets(self,dict):
        dict['id'] = self.id
        self.pets.append(dict)
    # def pets(self,name,type,age,owner,vaccinated = False):
    #     self.pets.append(
    #         {
    #          "id": self.id,
    #          "name": name,
    #          "type": type,
    #          "age": age,
    #          "owner": owner,
    #          "vaccinated": vaccinated
    #          }
    #     )
    #     self.id +=1

if __name__ == "__main__":
    pet = Pet()
    print(pet.pets)
    pet.pets = {"id": 1, "name": "Барсик", "type": "кот", "age": 3, "owner": "Мария", "vaccinated": True}
    print(pet.pets)
