from Task8_peewee.Models.Employees import *

class EmploeesController:
    '''
    добавить сотрудника,
    повысить зарплату,
    сотрудники отдела,
    уволить
    '''
    @classmethod
    # добавить сотрудника,
    def add(cls,name,position,salary,department):
        Employees.create(
            name = name,
            position = position,
            salary = salary,
            department = department,
        )
    @classmethod
    #повысить зарплату,
    def salary_update(cls,id,salary):
        Employees.update({Employees.salary:salary}).where(Employees.id == id).execute()
    @classmethod
    def get_departament(cls,department):
        #сотрудники отдела
        return Employees.select().where(Employees.department==department)
    @classmethod
    #уволить
    def delite(cls,id):
        Employees.delete_by_id(id)
if __name__ == '__main__':
    (EmploeesController
     .add("viktor", 'fklv', 10000, "flfj"))
