class MyTasks:
    '''
    Управлять списком задач с полями: id, задача, статус (выполнено/невыполнено)
    '''

    def __init__(self):
        '''
        метод конструктор в котором задаю атрибуты список дел и идентификаторы дел
        список дел состоит из словарей и т.д
        '''
        self.__tasks = [
            {"id": 1, "task": "Анна", "age": 20, "grade": "A","completed": False},
            {"id": 2, "task": "Петр", "age": 19, "grade": "B","completed": True}
        ]  # атрибут класса - список с двумя Делами
        self.id = 3  # атррибут класа- для автоматического создания id
        # методы CRUD - Create, Read, Update, Delete

    def add(self, task):
        '''
        создает новое дело в виде словаря {"id": 1, "task": "Купить молоко", "completed": False}
        и добавляет список атрибута self.tasks
        :param
            task(str): Дело в виде строки
            id(int): создается автоматически с помощью атрибута self.id
            completed(boolean): автоматически присвается False
        :returns:
            True
        '''
        self.tasks.append(
            {
                "id": self.id,
                "task": task,
                "completed": False
            }
        )
        self.id += 1 # увеличить на 1, следующий id будет на 1 больше
        return True
    # показать всё - Read
    @property
    def tasks(self):
        '''
        выводит информацию о делах
        :return: список словарей с делами
        '''
        return self.__tasks

    # отметить выполниной - update
    def completed(self,id):
        '''
        меняет значение complited на True у словаря с id == id гз аргумента
        :params id: словаярь с данным id
        :returns:
            Task - словарь
        '''
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
    task = MyTasks()
    print(task.tasks)
    print(task.tasks)
    print(task.completed(1))
    print(task.tasks)
    task.delete(1)
    print(task.tasks)