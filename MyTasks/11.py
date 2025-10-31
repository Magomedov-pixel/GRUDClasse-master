class MyTasks:

    def __init__(self):
        self.__events = [
            {"id": 1, "title": "Встреча", "date": "2024-02-15", "time": "14:00",
             "description": "С коллегами"}
        ]

        self.id = 2

    def add(self, title):
        self.events.append(
            {
                "id": self.id,
                "title": title,
                "completed": False
            }
        )
        self.id += 1  # увеличить на 1, следующий id будет на 1 больше
        return True

    # показать всё - Read
    @property
    def events(self):
        return self.__events

    # отметить выполниной - update
    def completed(self, id):
        for dict in self.__events:
            if dict['id'] == id:
                dict['completed'] = True
                return dict

    # удалить
    def delete(self, id):
        for dict in self.__events:
            if dict['id'] == id:
                self.__events.remove(dict)


if __name__ == "__main__":
    title = MyTasks()
    print(title.events)
    print(title.events)
    print(title.completed(1))
    print(title.events)
    title.delete(1)
    print(title.events)
