from Task12_peewee.Model.Recipes import *

class RecipesController:
    '''
    добавить проект,
    изменить статус,
    проекты по приоритету
    '''
    @classmethod
    def add(cls, name, status, deadline, priority):
        # добавить книгу
        Recipes.create(
            name=name,
            status=status,
            deadline=deadline,
            priority=priority
        )
    @classmethod
    def status_update(cls, id, status):
        # изменить статус
        Recipes.update({Recipes.status: status}).where(Recipes.id == id).execute()
    @classmethod
    def get_priority(cls, priority):
        # проекты по приоритету
        return Recipes.select().where(Recipes.priority == priority)

if __name__ == '__main__':
    RecipesController.add(
        "ads",
        'ads',
        'ads',
        'ads'
    )