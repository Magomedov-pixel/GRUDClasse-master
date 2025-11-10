from Task5_peewee.Models.Students import *

class StudentsController:
    '''
    CRUD
    добавить студента,
    изменить оценку,
    найти по имени,
    удалить
    '''
    @classmethod
    def add(cls,name,age,grade):
        # добавить студента
        Students.create(
            name = name,
            age = age,
            grade = grade,
        )
    @classmethod
    def grade_update(cls,id,grade):
        #изменить оценку
        Students.update({Students.grade:grade}).where(Students.id==id).execute()

    @classmethod
    def get_name(cls,name):
        #найти по имени
        return Students.select().where(Students.name==name)
    @classmethod
    #удалить
    def delite(cls,id):
        Students.delete_by_id(id)

if __name__ == '__main__':
    StudentsController.add(
        'Игорь',
        19,
        "A",
    )