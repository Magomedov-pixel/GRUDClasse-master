from tkinter import *
from tkinter import ttk

from Task11.Controllers.EventsControllers import EventsController


class EventsView(Tk):
    def __init__(self):
        super().__init__()
        self.title("база данных планировщик событий")
        self.geometry('1500x500')

        # раздел добавить
        self.fram_add = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.fram_add.pack(anchor='center', fill=X, padx=10, pady=10)
        self.add_title = ttk.Label(self.fram_add, text='добавить планировщик событий ')
        self.add_title.pack()

        # title
        self.title = ttk.Label(self.fram_add, text="введите событие")
        self.title.pack()
        # окна ввода title
        self.input_title = ttk.Entry(self.fram_add)
        self.input_title.pack()

        # date
        self.date = ttk.Label(self.fram_add, text="введите дату")
        self.date.pack()
        # окна ввода date
        self.input_date = ttk.Entry(self.fram_add)
        self.input_date.pack()

        # time
        self.time = ttk.Label(self.fram_add, text="Введите время")
        self.time.pack()
        # Окна ввода данных time
        self.input_time = ttk.Entry(self.fram_add)
        self.input_time.pack()

        # description
        self.description = ttk.Label(self.fram_add, text="Введите описание")
        self.description.pack()
        # Окна ввода данных description
        self.input_description = ttk.Entry(self.fram_add)
        self.input_description.pack()

        # кнопка
        self.add_button = ttk.Button(self.fram_add, text='добавить', command=self.add_ev)
        self.add_button.pack()

        # таблица
        self.fram_table = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.fram_table.pack(anchor='center', fill=X, padx=10, pady=10)
        columns = ('id', 'title', 'date', 'time', 'description')
        self.tree = ttk.Treeview(self.fram_table,columns=columns,show="headings")
        self.tree.pack(fill=BOTH, expand=1)
        self.table()
    def table(self):
        # очистить таблицу
        for item in self.tree.get_children():
            self.tree.delete(item)

        events = EventsController.get()
        list_events = []
        for meal in events:
            list_events.append(
                (
                    meal['id'],
                    meal['title'],
                    meal['date'],
                    meal['time'],
                    meal['description'],
                 )
            )

        # перевести на русский язык названия столбцов
        self.tree.heading('id',text='№')
        self.tree.heading('title',text='событие')
        self.tree.heading('date',text='дата')
        self.tree.heading('time', text='время')
        self.tree.heading('description', text='описание')

        for events in list_events:
            self.tree.insert('',END,values=events)

    # вывод
    def add_ev(self):
        EventsController.add(
            title=self.input_title.get(),
            date=self.input_date.get(),
            time=self.input_time.get(),
            description=self.input_description.get(),
        )
        self.table()
