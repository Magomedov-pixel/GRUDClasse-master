from tkinter import *
from tkinter import ttk

from Task8.Controllers.EmployeesControllers import EmployeeController


class EmployeesView(Tk):
    def __init__(self):
        super().__init__()
        self.title("база данных сотрудников компании")
        self.geometry('1500x500')

        # раздел добавить
        self.fram_add = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.fram_add.pack(anchor='center', fill=X, padx=10, pady=10)
        self.add_title = ttk.Label(self.fram_add, text='добавить сотрудника')
        self.add_title.pack()

        # name
        self.name = ttk.Label(self.fram_add, text="введите имя")
        self.name.pack()
        # окна ввода name
        self.input_name = ttk.Entry(self.fram_add)
        self.input_name.pack()

        # position
        self.position = ttk.Label(self.fram_add, text="введите должность")
        self.position.pack()
        # окна ввода position
        self.input_position = ttk.Entry(self.fram_add)
        self.input_position.pack()

        # salary
        self.salary = ttk.Label(self.fram_add, text="Введите зп")
        self.salary.pack()
        # Окна ввода данных salary
        self.input_salary = ttk.Entry(self.fram_add)
        self.input_salary.pack()

        # department
        self.department = ttk.Label(self.fram_add, text="Введите отдел")
        self.department.pack()
        # Окна ввода данных department
        self.input_department = ttk.Entry(self.fram_add)
        self.input_department.pack()

        # кнопка
        self.add_button = ttk.Button(self.fram_add, text='добавить', command=self.add_emp)
        self.add_button.pack()

        # таблица
        self.fram_table = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.fram_table.pack(anchor='center', fill=X, padx=10, pady=10)
        columns = ('id', 'name', 'position', 'salary', 'department')
        self.tree = ttk.Treeview(self.fram_table,columns=columns,show="headings")
        self.tree.pack(fill=BOTH, expand=1)
        self.table()
    def table(self):
        # очистить таблицу
        for item in self.tree.get_children():
            self.tree.delete(item)

        employees = EmployeeController.get()
        list_employees = []
        for empl in employees:
            list_employees.append(
                (
                    empl['id'],
                    empl['name'],
                    empl['position'],
                    empl['salary'],
                    empl['department'],
                 )
            )

        # перевести на русский язык названия столбцов
        self.tree.heading('id',text='№')
        self.tree.heading('name',text='имя')
        self.tree.heading('position',text='должность')
        self.tree.heading('salary', text='зп')
        self.tree.heading('department', text='отдел')

        for employees in list_employees:
            self.tree.insert('',END,values=employees)

    # вывод
    def add_emp(self):
        EmployeeController.add(
            name=self.input_name.get(),
            position=self.input_position.get(),
            salary=self.input_salary.get(),
            department=self.input_department.get(),
        )
        self.table()
