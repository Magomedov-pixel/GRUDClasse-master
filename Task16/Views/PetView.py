from tkinter import *
from tkinter import ttk

from Task16.Controllers.PetComtroller import PetController


class PetView(Tk):
    def __init__(self):
        super().__init__()
        self.title("учет домашних животных")
        self.geometry('1500x500')

        # раздел добавить
        self.fram_add = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.fram_add.pack(anchor='center', fill=X, padx=10, pady=10)
        self.add_title = ttk.Label(self.fram_add, text='добавить питомца')
        self.add_title.pack()

        # name
        self.name = ttk.Label(self.fram_add, text="введите имя питомца")
        self.name.pack()
        # окна ввода name
        self.input_name = ttk.Entry(self.fram_add)
        self.input_name.pack()

        # type
        self.type = ttk.Label(self.fram_add, text="введите тип питомца")
        self.type.pack()
        # окна ввода type
        self.input_type = ttk.Entry(self.fram_add)
        self.input_type.pack()

        # age
        self.age = ttk.Label(self.fram_add, text="введите возраст питомца")
        self.age.pack()
        # окна ввода age
        self.input_age = ttk.Entry(self.fram_add)
        self.input_age.pack()

        # owner
        self.owner = ttk.Label(self.fram_add, text="введите имя хозяина питомца")
        self.owner.pack()
        # окна ввода owner
        self.input_owner = ttk.Entry(self.fram_add)
        self.input_owner.pack()

        # кнопка
        self.add_button = ttk.Button(self.fram_add, text='добавить', command=self.add_pet)
        self.add_button.pack()

        # таблица
        self.fram_table = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.fram_table.pack(anchor='center', fill=X, padx=10, pady=10)
        columns = ('id', 'name', 'type', 'age', 'owner', 'vaccinated')
        self.tree = ttk.Treeview(self.fram_table,columns=columns,show="headings")
        self.tree.pack(fill=BOTH, expand=1)
        self.table()
    def table(self):
        # очистить таблицу
        for item in self.tree.get_children():
            self.tree.delete(item)
        # список животных
        pets = PetController.get()
        list_pets = [] # сюда будут передоватся картежи с описанием животных
        for pet in pets:
            list_pets.append(
                (
                    pet['id'],
                    pet['name'],
                    pet['type'],
                    pet['age'],
                    pet['owner'],
                    pet['vaccinated'],
                 )
            )

        # перевести на русский язык названия столбцов
        self.tree.heading('id',text='№')
        self.tree.heading('name',text='имя')
        self.tree.heading('type',text='тип')
        self.tree.heading('age',text='возраст')
        self.tree.heading('owner',text='имя хозяина')
        self.tree.heading('vaccinated',text='вакцинация')
        for pet in list_pets:
            self.tree.insert('',END,values=pet)

    # вывод
    def add_pet(self):
        PetController.add(
            name=self.input_name.get(),
            type=self.input_type.get(),
            age=self.input_age.get(),
            owner=self.input_owner.get()
        )
        self.table()
        print(PetController.get())
#