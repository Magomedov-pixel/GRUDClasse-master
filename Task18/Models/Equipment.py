class Equipment:
    '''
    добавить оборудование,
    изменить статус,
    найти по пользователю,
    списать
    '''

    def __init__(self):
        self.__list_equipment = [
            {
                "id": 1,
                "name": "Ноутбук Dell",
                "type": "ноутбук",
                "serial": "ABC123",
                "status": "в работе",
                "user": "Петр"}
        ]
        self.id = 2

    @property
    def equipment(self):
        return self.__list_equipment

    @equipment.setter
    def equipment(self, dict):
        dict['id'] = self.id
        self.equipment.append(dict)


if __name__ == '__main__':
    equi = Equipment()
    print(equi.equipment)
    equi.equipment = {"id": 2, "name": "Ноутбук Dell", "type": "ноутбук", "serial": "ABC123", "status": "в работе", "user": "Петр"}
    print(equi.equipment)
