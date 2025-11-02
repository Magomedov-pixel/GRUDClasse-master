class Recipe:
    def __init__(self):
        self.__list_recipes = [
            {"id": 1,
             "name": "Борщ",
             "ingredients": ["свекла", "капуста", "мясо"],
             "cooking_time": 120,
             "difficulty": "средняя"}
        ]
        self.id = 2
    @property
    def recipes(self):
        return self.__list_recipes

    @recipes.setter
    def recipes(self, dict):
        dict['id'] = self.id
        self.recipes.append(dict)
        self.id += 1

if __name__ == '__main__':
    rec = Recipe()
    print(rec.recipes)