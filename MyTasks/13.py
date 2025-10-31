class MyTasks_12:
    def __init__(self):
        self.__projects = [
            {"id": 1, "name": "Веб-сайт", "status": "в процессе", "deadline": "2024-03-01", "priority": "высокий"}
        ]
        self.id = 3

    def add(self, name):

        self.projects.append(
            {
                "id": self.id,
                "name": name,
                "completed": False
            }
        )
        self.id += 1
        return True

    @property
    def projects(self):

        return self.__projects

    def completed(self, id):

        for dict in self.__projects:
            if dict['id'] == id:
                dict['completed'] = True
                return dict

    def delete(self, id):
        for dict in self.__projects:
            if dict['id'] == id:
                self.__projects.remove(dict)


if __name__ == "__main__":
    name = MyTasks_12()
    print(name.projects)
    name.add("Сходить в ЯМК")
    print(name.projects)
    print(f"метод изменить статус", name.completed(1))
    print(name.projects)
    name.delete(1)
    print(name.projects)
