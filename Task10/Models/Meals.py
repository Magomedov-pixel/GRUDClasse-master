class Meals:
    def __init__(self):
        self.__list_meals = [
            {"id": 1, "meal": "Завтрак", "food": "Овсянка", "calories": 300, "time":"08:00"}
        ]
        self.id = 2
    @property
    def meals(self):
        return self.__list_meals
    @meals.setter
    def meals(self, dict):
        dict['id'] = self.id
        self.meals.append(dict)
        self.id += 1

if __name__ == '__main__':
    mel = Meals()
    print(mel.meals)
    mel.meals = {"meal": "Обед", "food": "Суп гороховый", "calories": 500, "time":"12:00"}
    print(mel.meals)