from tkinter import *
from tkinter import ttk

from Task1.Controllers.TaskControllers import TaskController


class TaskView(Tk):

    def __init__(self):
        super().__init__()
        self.title("список задач")
        self.geometry('1500x500')

        # раздел Добавить
        self.fram_add = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.fram_add.pack(anchor='center', fill=X, padx=10, pady=10)

        self.add_title = ttk.Label(self.fram_add, text="добавить задачу")
        self.add_title.pack()

        # task
        self.task = ttk.Label(self.fram_add, text="задача")
        self.task.pack()

        # Окна ввода данных
        self.input_task = ttk.Entry(self.fram_add)
        self.input_task.pack()

        # Кнопка
        self.add_button = ttk.Button(self.fram_add, text="Добавить", command=self.add_tas)
        self.add_button.pack()
        # вывод
        #Таблица
        self.frame_table = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.frame_table.pack(anchor='center', fill=X, padx=10, pady=10)


        columns = ('id','task')
        self.tree =ttk.Treeview(self.frame_table,columns=columns,show="headings")
        self.tree.pack(fill=BOTH,expand=1)
        self.table()

    def table(self):
        # Очистить таблицу
        for item in self.tree.get_children():
            self.tree.delete(item)

        tasks = TaskController.get()
        list_task = [] # суда будут передаваться кортежи с описанием животных
        for tasks in tasks:
            list_task.append(
                (
                    tasks['id'],
                    tasks['task'],
                    # tasks['completed'],
                 )
            )
        # перевести на русский язык названия столбцов
        self.tree.heading('id', text="№")
        self.tree.heading('task', text="задача")
        for pet in list_task:
            self.tree.insert("",END,values=pet)

    def add_tas(self):
        TaskController.add(
            task=self.input_task.get(),
        )
        self.table()