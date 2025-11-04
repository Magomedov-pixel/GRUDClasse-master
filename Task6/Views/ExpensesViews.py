from tkinter import *
from tkinter import ttk

from Task6.Controllers.ExpensesControllers import ExpensesController


class ExpensesView(Tk):
    def __init__(self):
        super().__init__()
        self.title("база данных расходов")
        self.geometry('1500x500')

        # раздел добавить
        self.fram_add = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.fram_add.pack(anchor='center', fill=X, padx=10, pady=10)
        self.add_title = ttk.Label(self.fram_add, text='добавить расход')
        self.add_title.pack()

        # amount
        self.amount = ttk.Label(self.fram_add, text="введите цена")
        self.amount.pack()
        # окна ввода amount
        self.input_amount = ttk.Entry(self.fram_add)
        self.input_amount.pack()

        # category
        self.category = ttk.Label(self.fram_add, text="введите категория")
        self.category.pack()
        # окна ввода category
        self.input_category = ttk.Entry(self.fram_add)
        self.input_category.pack()

        # date
        self.date = ttk.Label(self.fram_add, text="Введите дату")
        self.date.pack()
        # Окна ввода данных date
        self.input_date = ttk.Entry(self.fram_add)
        self.input_date.pack()

        # description
        self.description = ttk.Label(self.fram_add, text="Введите описание")
        self.description.pack()
        # Окна ввода данных description
        self.input_description = ttk.Entry(self.fram_add)
        self.input_description.pack()

        # кнопка
        self.add_button = ttk.Button(self.fram_add, text='добавить', command=self.add_exp)
        self.add_button.pack()

        # таблица
        self.fram_table = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.fram_table.pack(anchor='center', fill=X, padx=10, pady=10)
        columns = ('id', 'amount', 'category', 'date', 'description')
        self.tree = ttk.Treeview(self.fram_table,columns=columns,show="headings")
        self.tree.pack(fill=BOTH, expand=1)
        self.table()
    def table(self):
        # очистить таблицу
        for item in self.tree.get_children():
            self.tree.delete(item)

        expense = ExpensesController.get()
        list_expenses = []
        for expe in expense:
            list_expenses.append(
                (
                    expe['id'],
                    expe['amount'],
                    expe['category'],
                    expe['date'],
                    expe['description'],
                 )
            )

        # перевести на русский язык названия столбцов
        self.tree.heading('id',text='№')
        self.tree.heading('amount',text='цена')
        self.tree.heading('category',text='категория')
        self.tree.heading('date', text='дата')
        self.tree.heading('description', text='описание')

        for expense in list_expenses:
            self.tree.insert('',END,values=expense)

    # вывод
    def add_exp(self):
        ExpensesController.add(
            amount=self.input_amount.get(),
            category=self.input_category.get(),
            date=self.input_date.get(),
            description=self.input_description.get()

        )
        self.table()
