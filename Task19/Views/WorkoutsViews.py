from tkinter import *
from tkinter import ttk

from Task19.Controllers.WorkoutsController import WorkoutsController

class WorkoutsView(Tk):
    def __init__(self):
        super().__init__()
        self.title('база данных учет спортивных занятий')
        self.geometry('800x800')

        # раздел добавить
        self.fram_add = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.fram_add.pack(anchor='center', fill=X, padx=10, pady=10)
        self.add_title = ttk.Label(self.fram_add, text='добавить спортивные занятия')
        self.add_title.pack()

        # date
        self.date = ttk.Label(self.fram_add, text="введите дату")
        self.date.pack()
        # окна ввода date
        self.input_date = ttk.Entry(self.fram_add)
        self.input_date.pack()

        # type
        self.type = ttk.Label(self.fram_add, text="введите тип спортивного занятия")
        self.type.pack()
        # окна ввода type
        self.input_type = ttk.Entry(self.fram_add)
        self.input_type.pack()

        # duration
        self.duration = ttk.Label(self.fram_add, text="введите продолжительность занятия")
        self.duration.pack()
        # окна ввода duration
        self.input_duration = ttk.Entry(self.fram_add)
        self.input_duration.pack()

        # calories
        self.calories = ttk.Label(self.fram_add, text="введите потерянные калории")
        self.calories.pack()
        # окна ввода calories
        self.input_calories = ttk.Entry(self.fram_add)
        self.input_calories.pack()

        # notes
        self.notes = ttk.Label(self.fram_add, text="введите время")
        self.notes.pack()
        # окна ввода notes
        self.input_notes = ttk.Entry(self.fram_add)
        self.input_notes.pack()

        # кнопка
        self.add_button = ttk.Button(self.fram_add, text='добавить', command=self.add_mel)
        self.add_button.pack()

        # таблица
        self.fram_table = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.fram_table.pack(anchor='center', fill=X, padx=10, pady=10)
        columns = ('id', 'date', 'type', 'duration', 'calories','notes')
        self.tree = ttk.Treeview(self.fram_table, columns=columns, show="headings")
        self.tree.pack(fill=BOTH, expand=1)
        self.table()

    def table(self):
        # очистить таблицу
        for item in self.tree.get_children():
            self.tree.delete(item)

        workouts = WorkoutsController.get()
        list_workouts = []
        for workouts in workouts:
            list_workouts.append(
                (
                    workouts['id'],
                    workouts['date'],
                    workouts['type'],
                    workouts['duration'],
                    workouts['calories'],
                    workouts['notes'],
                )
            )

        # перевести на русский язык названия столбцов
        self.tree.heading('id', text='№')
        self.tree.heading('date', text='дата')
        self.tree.heading('type', text='тип')
        self.tree.heading('duration', text='продолжительность')
        self.tree.heading('calories', text='калории')
        self.tree.heading('notes', text='время')

        for workouts in list_workouts:
            self.tree.insert('', END, values=workouts)

        # вывод

    def add_mel(self):
        WorkoutsController.add(
            date=self.input_date.get(),
            type=self.input_type.get(),
            duration=self.input_duration.get(),
            calories=self.input_calories.get(),
            notes=self.input_notes.get(),
        )
        self.table()
