class Employee:
    def __init__ (self):
        self.__list_employees = [
            {
                "id": 1,
                "name": "Мария",
                "position": "Разработчик",
                "salary": 100000,
                "department": "IT"}
        ]
        self.id = 2
    @property
    def employees(self):
        return self.__list_employees
    @employees.setter
    def employees(self,dict):
        dict['id'] = self.id
        self.employees.append(dict)
        self.id +=1
if __name__ == '__main__':
    emp = Employee()