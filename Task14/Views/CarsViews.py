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