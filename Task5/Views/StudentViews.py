from tkinter import *
from tkinter import ttk

from Task5.Controllers.StudentsControllers import StudentsControllers


class StudentsView(Tk):
    def __init__(self):
        super().__init__()
        self.title("база данных студентов")
        self.geometry('1500x500')

        # раздел добавить
        self.fram_add = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.fram_add.pack(anchor='center', fill=X, padx=10, pady=10)
        self.add_title = ttk.Label(self.fram_add, text='добавить студента')
        self.add_title.pack()

        # name
        self.name = ttk.Label(self.fram_add, text="введите имя")
        self.name.pack()
        # окна ввода name
        self.input_name = ttk.Entry(self.fram_add)
        self.input_name.pack()

        # age
        self.age = ttk.Label(self.fram_add, text="введите возраст")
        self.age.pack()
        # окна ввода phone
        self.input_age = ttk.Entry(self.fram_add)
        self.input_age.pack()

        # grade
        self.grade = ttk.Label(self.fram_add, text="Введите оценку")
        self.grade.pack()
        # Окна ввода данных grade
        self.input_grade = ttk.Entry(self.fram_add)
        self.input_grade.pack()

        # кнопка
        self.add_button = ttk.Button(self.fram_add, text='добавить', command=self.add_stud)
        self.add_button.pack()

        # таблица
        self.fram_table = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.fram_table.pack(anchor='center', fill=X, padx=10, pady=10)
        columns = ('id', 'name', 'age', 'grade')
        self.tree = ttk.Treeview(self.fram_table,columns=columns,show="headings")
        self.tree.pack(fill=BOTH, expand=1)
        self.table()
    def table(self):
        # очистить таблицу
        for item in self.tree.get_children():
            self.tree.delete(item)

        students = StudentsControllers.get()
        list_students = []
        for stud in students:
            list_students.append(
                (
                    stud['id'],
                    stud['name'],
                    stud['age'],
                    stud['grade'],
                 )
            )

        # перевести на русский язык названия столбцов
        self.tree.heading('id',text='№')
        self.tree.heading('name',text='имя')
        self.tree.heading('age',text='возраст')
        self.tree.heading('grade', text='отценка')

        for students in list_students:
            self.tree.insert('',END,values=students)

    # вывод
    def add_stud(self):
        StudentsControllers.add(
            name=self.input_name.get(),
            age=self.input_age.get(),
            grade=self.input_grade.get(),

        )
        self.table()
