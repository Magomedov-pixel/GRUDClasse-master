class Students:
    def __init__(self):
        self.__list_students = [
            {"id": 1, "name": "Анна", "age": 20, "grade": "A"},
            {"id": 2, "name": "Петр", "age": 19, "grade": "B"}
        ]
        self.id = 3

    @property
    def students(self):
        return self.__list_students
    @students.setter
    def students(self, dict):
        dict['id'] = self.id
        self.students.append(dict)
        self.id +=1

if __name__ == '__main__':
    stud = Students()
    print(stud.students)
    stud.students = {"name":"Миша", "age": 20, "grade": "A"}
    print(stud.students)
