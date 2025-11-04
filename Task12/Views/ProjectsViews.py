from tkinter import *
from tkinter import ttk

from Task12.Controllers.ProjectsControllers import ProjectsController


class ProjectsView(Tk):
    def __init__(self):
        super().__init__()
        self.title("база данных управления проектами")
        self.geometry('1500x500')

        # раздел добавить
        self.fram_add = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.fram_add.pack(anchor='center', fill=X, padx=10, pady=10)
        self.add_title = ttk.Label(self.fram_add, text='добавить проект')
        self.add_title.pack()

        # name
        self.name = ttk.Label(self.fram_add, text="введите имя проекта")
        self.name.pack()
        # окна ввода name
        self.input_name = ttk.Entry(self.fram_add)
        self.input_name.pack()

        # status
        self.status = ttk.Label(self.fram_add, text="введите статус проекта")
        self.status.pack()
        # окна ввода status
        self.input_status = ttk.Entry(self.fram_add)
        self.input_status.pack()

        # deadline
        self.deadline = ttk.Label(self.fram_add, text="Введите дату")
        self.deadline.pack()
        # Окна ввода данных deadline
        self.input_deadline = ttk.Entry(self.fram_add)
        self.input_deadline.pack()

        # priority
        self.priority = ttk.Label(self.fram_add, text="Введите приоритет проекта")
        self.priority.pack()
        # Окна ввода данных priority
        self.input_priority = ttk.Entry(self.fram_add)
        self.input_priority.pack()

        # кнопка
        self.add_button = ttk.Button(self.fram_add, text='добавить', command=self.add_pr)
        self.add_button.pack()

        # таблица
        self.fram_table = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.fram_table.pack(anchor='center', fill=X, padx=10, pady=10)
        columns = ('id', 'name', 'status', 'deadline', 'priority')
        self.tree = ttk.Treeview(self.fram_table,columns=columns,show="headings")
        self.tree.pack(fill=BOTH, expand=1)
        self.table()
    def table(self):
        # очистить таблицу
        for item in self.tree.get_children():
            self.tree.delete(item)

        projects = ProjectsController.get()
        list_projects = []
        for pro in projects:
            list_projects.append(
                (
                    pro['id'],
                    pro['name'],
                    pro['status'],
                    pro['deadline'],
                    pro['priority'],
                 )
            )

        # перевести на русский язык названия столбцов
        self.tree.heading('id',text='№')
        self.tree.heading('name',text='имя проекта')
        self.tree.heading('status',text='статус проекта')
        self.tree.heading('deadline', text='дата проекта')
        self.tree.heading('priority', text='приоритет статуса')

        for projects in list_projects:
            self.tree.insert('',END,values=projects)

    # вывод
    def add_pr(self):
        ProjectsController.add(
            name=self.input_name.get(),
            status=self.input_status.get(),
            deadline=self.input_deadline.get(),
            priority=self.input_priority.get(),
        )
        self.table()
