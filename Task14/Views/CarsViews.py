from tkinter import *
from tkinter import ttk

from Task14.Controllers.CarsControllers import CarsController

class CarsViews(Tk):
    def __init__(self):
        super().__init__()
        self.title("База данных автомобилей")
        self.geometry('1500x500')

        # раздел добавить
        self.fram_add = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.fram_add.pack(anchor='center', fill=X, padx=10, pady=10)
        self.add_title = ttk.Label(self.fram_add, text='добавить автомобиль')
        self.add_title.pack()

        # brand
        self.brand = ttk.Label(self.fram_add, text="введите название бренда")
        self.brand.pack()
        # окна ввода brand
        self.input_brand = ttk.Entry(self.fram_add)
        self.input_brand.pack()

        # model
        self.model = ttk.Label(self.fram_add, text="введите модель")
        self.model.pack()
        # окна ввода model
        self.input_model = ttk.Entry(self.fram_add)
        self.input_model.pack()

        # year
        self.year = ttk.Label(self.fram_add, text="введите год выпуска")
        self.year.pack()
        # окна ввода year
        self.input_year = ttk.Entry(self.fram_add)
        self.input_year.pack()

        # color
        self.color = ttk.Label(self.fram_add, text="введите цвет авто")
        self.color.pack()
        # окна ввода color
        self.input_color = ttk.Entry(self.fram_add)
        self.input_color.pack()

        # price
        self.price = ttk.Label(self.fram_add, text="введите цену")
        self.price.pack()
        # окна ввода price
        self.input_price = ttk.Entry(self.fram_add)
        self.input_price.pack()

        # кнопка
        self.add_button = ttk.Button(self.fram_add, text='добавить', command=self.add_rec)
        self.add_button.pack()

        # таблица
        self.fram_table = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.fram_table.pack(anchor='center', fill=X, padx=10, pady=10)
        columns = ('id', 'brand', 'model','year','color','price')
        self.tree = ttk.Treeview(self.fram_table, columns=columns, show="headings")
        self.tree.pack(fill=BOTH, expand=1)
        self.table()

    def table(self):
        # очистить таблицу
        for item in self.tree.get_children():
            self.tree.delete(item)

        cars = CarsController.get()
        list_cars = []
        for cars in cars:
            list_cars.append(
                (
                    cars['id'],
                    cars['brand'],
                    cars['model'],
                    cars['year'],
                    cars['color'],
                    cars['price'],
                )
            )

        # перевести на русский язык названия столбцов
        self.tree.heading('id', text='№')
        self.tree.heading('brand', text='бренд')
        self.tree.heading('model', text='модель')
        self.tree.heading('year', text='год')
        self.tree.heading('color', text='цвет')
        self.tree.heading('price', text='цена')

        for cars in list_cars:
            self.tree.insert('', END, values=cars)

        # вывод

    def add_rec(self):
        CarsController.add(
            brand=self.input_brand.get(),
            model=self.input_model.get(),
            year=self.input_year.get(),
            color=self.input_color.get(),
            price=self.input_price.get(),
        )
        self.table()