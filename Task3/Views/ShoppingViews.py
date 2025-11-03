from tkinter import *
from tkinter import ttk

from Task3.Controllers.ShoppingControllers import ShoppingControllers


class ShoppingView(Tk):
    def __init__(self):
        super().__init__()
        self.title("учет продуктов")
        self.geometry('1500x500')

        # раздел добавить
        self.fram_add = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.fram_add.pack(anchor='center', fill=X, padx=10, pady=10)
        self.add_title = ttk.Label(self.fram_add, text='добавить покупки')
        self.add_title.pack()

        # product
        self.product = ttk.Label(self.fram_add, text="введите название продукта")
        self.product.pack()
        # окна ввода product
        self.input_product = ttk.Entry(self.fram_add)
        self.input_product.pack()

        # quantity
        self.quantity = ttk.Label(self.fram_add, text="введите кол-во")
        self.quantity.pack()
        # окна ввода phone
        self.input_quantity = ttk.Entry(self.fram_add)
        self.input_quantity.pack()

        # кнопка
        self.add_button = ttk.Button(self.fram_add, text='добавить', command=self.add_shop)
        self.add_button.pack()

        # таблица
        self.fram_table = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.fram_table.pack(anchor='center', fill=X, padx=10, pady=10)
        columns = ('id', 'product', 'quantity', 'bought',)
        self.tree = ttk.Treeview(self.fram_table,columns=columns,show="headings")
        self.tree.pack(fill=BOTH, expand=1)
        self.table()
    def table(self):
        # очистить таблицу
        for item in self.tree.get_children():
            self.tree.delete(item)

        shoppings = ShoppingControllers.get()
        list_shopping = []
        for con in shoppings:
            list_shopping.append(
                (
                    con['id'],
                    con['product'],
                    con['quantity'],
                    # con['bought'],
                 )
            )

        # перевести на русский язык названия столбцов
        self.tree.heading('id',text='№')
        self.tree.heading('product',text='продукт')
        self.tree.heading('quantity',text='кол-во')
        self.tree.heading('bought', text='некупленные/купленные')

        for shop in list_shopping:
            self.tree.insert('',END,values=shop)

    # вывод
    def add_shop(self):
        ShoppingControllers.add(
            product=self.input_product.get(),
            quantity=self.input_quantity.get(),

        )
        self.table()
