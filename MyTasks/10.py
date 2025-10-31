class MyTasks:
    def __init__(self):
        self.__meals = [
            {"id": 1, "meal": "Завтрак", "food": "Овсянка", "calories": 300, "time": "08:00"}
        ]
        self.id = 2

    def add(self, meal):
        self.meals.append(
            {
                "id": self.id,
                "meal": meal,
                "completed": False
            }
        )
        self.id += 1  # увеличить на 1, следующий id будет на 1 больше
        return True

    # показать всё - Read
    @property
    def meals(self):
        return self.__meals

    # отметить выполниной - update
    def completed(self, id):
        for dict in self.__meals:
            if dict['id'] == id:
                dict['completed'] = True
                return dict

    # удалить
    def delete(self, id):
        for dict in self.__meals:
            if dict['id'] == id:
                self.__meals.remove(dict)


if __name__ == "__main__":
    meal = MyTasks()
    print(meal.meals)
    print(meal.meals)
    print(meal.completed(1))
    print(meal.meals)
    meal.delete(1)
    print(meal.meals)
