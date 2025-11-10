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

