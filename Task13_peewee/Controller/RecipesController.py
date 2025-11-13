from Task13_peewee.Model.Recipes import *

class RecipesController:
    '''
    добавить рецепт,
    найти по ингредиенту,
    быстрые рецепты
    '''
    @classmethod
    def add(cls, name, ingredients, cooking_time,difficulty):
        # добавить рецепт,
        Recipes.create(
            name=name,
            ingredients=ingredients,
            cooking_time=cooking_time,
            difficulty=difficulty
        )
    @classmethod
    def get_ingredients(cls, ingredients):
        # найти по ингредиенту,
        return Recipes.select().where(Recipes.ingredients == ingredients)
if __name__ == '__main__':
    RecipesController.add(
        'kdkdk',
        'ldldldldld',
        455,
        'ldldll'
    )