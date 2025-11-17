from Task1_peewee.Models.Tasks import *

class TasksController:
    '''
    добавить,
    показать все,
    отметить выполненной,
    удалить
    '''
    @classmethod
    def add(cls,task,completed):
        # добавление
        Tasks.create(
            task = task,
            completed = completed
        )
    @classmethod
    def completed_update(cls, id, completed):
        #  отметить выполненной,
        Tasks.update({Tasks.completed: completed}).where(Tasks.id == id).execute()
    @classmethod
    def delite(cls, id):
        # удалить
        Tasks.delete_by_id(id)
if __name__ == '__main__':
    TasksController.add(
        'sclsc',
        False
    )