class Workouts:
    def __init__(self):
        self.__list_workouts = [
            {"id": 1,
             "date": "2024-01-20",
             "type": "бег",
             "duration": 45,
             "calories": 400,
             "notes": "Утренняя пробежка"}
        ]
        self.id = 2
    @property
    def workouts(self):
        return self.__list_workouts

    @workouts.setter
    def workouts(self, dict):
        dict['id'] = self.id
        self.workouts.append(dict)
        self.id += 1

if __name__ == '__main__':
    wor = Workouts()
    print(wor.workouts)