class MyTasks:

    def __init__(self):
        self.__tasks = [
            {"id": 1, "title": "1984", "author": "Оруэлл", "year": 1949, "read": False}
        ]
        self.id = 2

    def add(self, author):
        self.tasks.append(
            {
                "id": self.id,
                "author": author,
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
    author = MyTasks()
    print(author.tasks)
    print(author.tasks)
    print(author.completed(1))
    print(author.tasks)
    author.delete(1)
    print(author.tasks)