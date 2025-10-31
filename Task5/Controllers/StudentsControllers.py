from Task5.Models.Students import Students
class StudentsControllers():
    '''
     добавить студента,
     изменить оценку,
     найти по имени,
     удалить
    '''

    obj = Students()
    @classmethod
    def get(cls):
        return cls.obj.students

    #добавление
    @classmethod
    def add(cls, name, age, grade):
        cls.obj.students = {"name": name, "age": age, "grade": grade}
    #изменение оценки
    @classmethod
    def update(cls, id, new_grade):
        for dict in cls.get():
            if dict['id'] == id:
                dict['grade'] = new_grade
    #найти по имени
    @classmethod
    def name(cls, name):
        result = f"нет {name}"
        for dict in cls.get():
            if dict['name'] == name:
                result = f"есть {name}"
        return result
    #удаление по id
    @classmethod
    def delete(cls, id):
        for dict in cls.get():
            if dict['id'] == id:
                cls.get().remove(dict)

if __name__ == '__main__':
    StudentsControllers.add('Мага', 18, 'A')
    print(StudentsControllers.get())
    StudentsControllers.update(2,"N")
    print(StudentsControllers.get())
    StudentsControllers.delete(2)
    print(StudentsControllers.get())
    StudentsControllers.name("Анна")
    print(StudentsControllers.get())