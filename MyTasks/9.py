class MyTasks:

    def __init__(self):
        self.__tasks = [
            {"id": 1, "title": "The Witcher 3", "genre": "RPG", "platform": "PC","completed": True}
        ]
        self.id = 2

    def add(self, title):
        self.tasks.append(
            {
                "id": self.id,
                "title": title,
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
    title = MyTasks()
    print(title.tasks)
    print(title.tasks)
    print(title.completed(1))
    print(title.tasks)
    title.delete(1)
    print(title.tasks)