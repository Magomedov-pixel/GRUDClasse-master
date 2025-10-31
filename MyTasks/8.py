class MyTasks:

    def __init__(self):
        self.__tasks = [
            {"id": 1, "name": "Мария", "position": "Разработчик", "salary": 100000,"department": "IT"}

        ]
        self.id = 2

    def add(self, name):
        self.tasks.append(
            {
                "id": self.id,
                "name": name,
                "completed": False
            }
        )
        self.id += 1 # увеличить на 1, следующий id будет на 1 больше
        return True
    # показать всё - Read
    @property
    def tasks(self):
        return self.__tasks

    # отметить выполниной - update
    def completed(self,id):
        for dict in self.__tasks:
            if  dict['id'] == id:
                dict['completed'] = True
                return dict
    # удалить
    def delete(self,id):
        for dict in self.__tasks:
            if dict['id'] == id:
                self.__tasks.remove(dict)

if __name__ == "__main__":
    name = MyTasks()
    print(name.tasks)
    print(name.tasks)
    print(name.completed(1))
    print(name.tasks)
    name.delete(1)
    print(name.tasks)