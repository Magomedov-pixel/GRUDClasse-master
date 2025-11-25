from tkinter import *
from tkinter import ttk

from Task15.Controllers.OrdersControllers import OrderController

class OrdersViews(Tk):
    def __init__(self):
        super().__init__()
        self.title("База данных Учет заказов в магазине")
        self.geometry('1500x500')

        # раздел добавить
        self.fram_add = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.fram_add.pack(anchor='center', fill=X, padx=10, pady=10)
        self.add_title = ttk.Label(self.fram_add, text='добавить заказ')
        self.add_title.pack()

        # customer
        self.customer = ttk.Label(self.fram_add, text="введите имя заказчика")
        self.customer.pack()
        # окна ввода customer
        self.input_customer = ttk.Entry(self.fram_add)
        self.input_customer.pack()

        # product
        self.product = ttk.Label(self.fram_add, text="введите продукт")
        self.product.pack()
        # окна ввода product
        self.input_product = ttk.Entry(self.fram_add)
        self.input_product.pack()

        # amount
        self.amount = ttk.Label(self.fram_add, text="введите кол-во")
        self.amount.pack()
        # окна ввода amount
        self.input_amount = ttk.Entry(self.fram_add)
        self.input_amount.pack()

        # order_date
        self.order_date = ttk.Label(self.fram_add, text="введите дату")
        self.order_date.pack()
        # окна ввода order_date
        self.input_order_date = ttk.Entry(self.fram_add)
        self.input_order_date.pack()

        # кнопка
        self.add_button = ttk.Button(self.fram_add, text='добавить', command=self.add_rec)
        self.add_button.pack()

        # таблица
        self.fram_table = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.fram_table.pack(anchor='center', fill=X, padx=10, pady=10)
        columns = ('id', 'customer', 'product','amount','order_date')
        self.tree = ttk.Treeview(self.fram_table, columns=columns, show="headings")
        self.tree.pack(fill=BOTH, expand=1)
        self.table()

    def table(self):
        # очистить таблицу
        for item in self.tree.get_children():
            self.tree.delete(item)

        orders = OrderController.get()
        list_orders = []
        for orders in orders:
            list_orders.append(
                (
                    orders['id'],
                    orders['customer'],
                    orders['product'],
                    orders['amount'],
                    orders['order_date'],
                )
            )

        # перевести на русский язык названия столбцов
        self.tree.heading('id', text='№')
        self.tree.heading('customer', text='заказчик')
        self.tree.heading('product', text='продукт')
        self.tree.heading('amount', text='кол-во')
        self.tree.heading('order_date', text='дата')
        for cars in list_orders:
            self.tree.insert('', END, values=cars)

        # вывод

    def add_rec(self):
        OrderController.add(
            customer=self.input_customer.get(),
            product=self.input_product.get(),
            amount=self.input_amount.get(),
            order_date=self.input_order_date.get(),
        )
        self.table()