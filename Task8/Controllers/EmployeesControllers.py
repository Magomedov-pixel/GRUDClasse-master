from Task8.Models.Employees import Employee
class EmployeeController:
    '''
    добавить сотрудника,
    повысить зарплату,
    сотрудники отдела,
    уволить
    '''
    obj = Employee()
    @classmethod
    def get(cls):
        return cls.obj.employees
    @classmethod
    def add(cls,name,position,department):
        cls.obj.employees ={"name":name,"position":position,"department":department}
    @classmethod
    def up_salary(cls,id,new_salary):
        for dict in cls.get():
            if dict['id'] == id:
                dict['salary'] = new_salary
    @classmethod
    def delete(cls, id):
        for dict in cls.get():
            if dict['id'] == id:
                cls.get().remove(dict)
if __name__ == '__main__':
    print(EmployeeController.get())
    EmployeeController.up_salary(1,100000000)
    print(EmployeeController.get())