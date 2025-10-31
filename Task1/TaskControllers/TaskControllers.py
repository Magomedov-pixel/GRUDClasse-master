from Task1.Models.Task import Task

class TaskController():
    '''
    управление в классе Task
        добавить,
        показать все,
        удалить
    '''
    obj = Task()
    @classmethod
    def get(cls):
        return cls.obj.tasks

    #добавление задачи
    @classmethod
    def add(cls,task):
        cls.obj.tasks = {"task": task}
# completed
    # удалить контакт
    @classmethod
    def delete(cls, id):
        for dict in cls.get():
            if dict['id'] == id:
                cls.get().remove(dict)

if __name__=="__main__":
    TaskController.add("погулять")
    print(TaskController.get())
    TaskController.delete(1)
    print(TaskController.get())
