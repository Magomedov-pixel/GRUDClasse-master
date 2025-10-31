class Task:
    def __init__(self):
        self.__list_task =[
            {"id": 1, "task": "Купить молоко", "completed": False},
            {"id": 2, "task": "Сделать уроки", "completed": True}
        ]
        self.id = 3

    @property
    def tasks(self):
        return self.__list_task
    @tasks.setter
    def tasks(self,dict):
        dict['id'] = self.id
        self.tasks.append(dict)
        self.id += 1

if __name__ == '__main__':
    tas = Task()
    print(tas.tasks)
    tas.tasks = {"task":"пойти погулять"}
    print(tas.tasks)