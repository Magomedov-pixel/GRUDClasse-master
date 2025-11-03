from tkinter import *
from tkinter import ttk

from Task2.Controllers.ContactController import ContactController


class ContactView(Tk):
    def __init__(self):
        super().__init__()
        self.title("учет номеров")
        self.geometry('1500x500')

        # раздел добавить
        self.fram_add = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.fram_add.pack(anchor='center', fill=X, padx=10, pady=10)
        self.add_title = ttk.Label(self.fram_add, text='добавить контакт')
        self.add_title.pack()

        # name
        self.name = ttk.Label(self.fram_add, text="введите имя контакта")
        self.name.pack()
        # окна ввода name
        self.input_name = ttk.Entry(self.fram_add)
        self.input_name.pack()

        # phone
        self.phone = ttk.Label(self.fram_add, text="введите номер контакта")
        self.phone.pack()
        # окна ввода phone
        self.input_phone = ttk.Entry(self.fram_add)
        self.input_phone.pack()

        # email
        self.email = ttk.Label(self.fram_add, text="введите эмаил контакта")
        self.email.pack()
        # окна ввода email
        self.input_email = ttk.Entry(self.fram_add)
        self.input_email.pack()

        # кнопка
        self.add_button = ttk.Button(self.fram_add, text='добавить', command=self.add_con)
        self.add_button.pack()

        # таблица
        self.fram_table = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.fram_table.pack(anchor='center', fill=X, padx=10, pady=10)
        columns = ('id', 'name', 'phone', 'email',)
        self.tree = ttk.Treeview(self.fram_table,columns=columns,show="headings")
        self.tree.pack(fill=BOTH, expand=1)
        self.table()
    def table(self):
        # очистить таблицу
        for item in self.tree.get_children():
            self.tree.delete(item)
        # список животных
        contacts = ContactController.get()
        list_contacts = [] # сюда будут передоватся картежи с описанием животных
        for con in contacts:
            list_contacts.append(
                (
                    con['id'],
                    con['name'],
                    con['phone'],
                    con['email'],
                 )
            )

        # перевести на русский язык названия столбцов
        self.tree.heading('id',text='№')
        self.tree.heading('name',text='имя')
        self.tree.heading('phone',text='телефон')
        self.tree.heading('email',text='эмаил')
        for pet in list_contacts:
            self.tree.insert('',END,values=pet)

    # вывод
    def add_con(self):
        ContactController.add(
            name=self.input_name.get(),
            phone=self.input_phone.get(),
            email=self.input_email.get(),
        )
        self.table()
