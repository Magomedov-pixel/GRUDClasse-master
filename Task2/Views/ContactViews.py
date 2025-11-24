from tkinter import *
from tkinter import ttk

from Task2.Controllers.ContactController import ContactController


class ContactView(Tk):

    def __init__(self):
        super().__init__()
        self.title("Система для хранения контактов")
        self.geometry('1500x500')

        # раздел Добавить
        self.fram_add = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.fram_add.pack(anchor='center', fill=X, padx=10, pady=10)

        self.add_title = ttk.Label(self.fram_add, text="добавить контакт")
        self.add_title.pack()

        # name
        self.name = ttk.Label(self.fram_add, text="имя")
        self.name.pack()
        # Окна ввода данных
        self.input_name = ttk.Entry(self.fram_add)
        self.input_name.pack()

        # phone
        self.phone = ttk.Label(self.fram_add, text="номер")
        self.phone.pack()
        # Окна ввода данных
        self.input_phone = ttk.Entry(self.fram_add)
        self.input_phone.pack()

        # email
        self.email = ttk.Label(self.fram_add, text="email")
        self.email.pack()
        # Окна ввода данных
        self.input_email = ttk.Entry(self.fram_add)
        self.input_email.pack()

        # Кнопка
        self.add_button = ttk.Button(self.fram_add, text="Добавить", command=self.add_tas)
        self.add_button.pack()
        # вывод
        #Таблица
        self.frame_table = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.frame_table.pack(anchor='center', fill=X, padx=10, pady=10)


        columns = ('id','name','phone','email')
        self.tree =ttk.Treeview(self.frame_table,columns=columns,show="headings")
        self.tree.pack(fill=BOTH,expand=1)
        self.table()

    def table(self):
        # Очистить таблицу
        for item in self.tree.get_children():
            self.tree.delete(item)

        contacts = ContactController.get()
        list_contact = [] # суда будут передаваться кортежи с описанием животных
        for contacts in contacts:
            list_contact.append(
                (
                    contacts['id'],
                    contacts['name'],
                    contacts['phone'],
                    contacts['email']

                    # tasks['completed'],
                 )
            )
        # перевести на русский язык названия столбцов
        self.tree.heading('id', text="№")
        self.tree.heading('name', text="имя")
        self.tree.heading('phone', text="номер")
        self.tree.heading('email', text="имэил")
        for pet in list_contact:
            self.tree.insert("",END,values=pet)

    def add_tas(self):
        ContactController.add(
            name=self.input_name.get(),
            phone=self.input_phone.get(),
            email=self.input_email.get(),
        )
        self.table()