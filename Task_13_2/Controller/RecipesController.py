from Task_13_2.Model.RecipesModel import RecipesModel
class RecipesController:
    obj = RecipesModel()
    @classmethod
    def get(cls):
        return cls.obj.recipes
    @classmethod
    def add(cls,name,cooking_time,difficulty,*ingredients):
        # new_ingredients = []
        # for elemnt in ingredients:
        #     new_ingredients.append(elemnt)
        # new_new_ingredients = [element for element in ingredients]
        dict = {
            "name":name,
            "ingredients": list(ingredients),#[element for element in ingredients]
            "cooking_time":cooking_time,
            "difficulty":difficulty
                }
        cls.obj.recipes = dict
        return dict
if __name__ == "__main__":
    print(RecipesController.get())
