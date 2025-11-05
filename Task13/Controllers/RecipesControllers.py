from  Task13.Models.Recipes import Recipe
class RecipesController:
    '''
    добавить рецепт, найти по ингредиенту, быстрые рецепты
    '''
    obj = Recipe()
    @classmethod
    def get(cls):
        return cls.obj.recipes
    @classmethod
    def add(cls,name,ingredients):
        cls.obj.recipes = {"name": name,"ingredients": ingredients,}

    @classmethod
    def ingredients(cls, ingredients):
        result = f"нет {ingredients}"
        for dict in cls.get():
            if dict['ingredients'] == ingredients:
                result = f"есть {ingredients}"
        return result
if __name__ == '__main__':
    print(RecipesController.get())