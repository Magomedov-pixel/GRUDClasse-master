from tkinter import *
from tkinter import ttk

from Task10.Controllers.MealsControllers import MealsController


class MealsView(Tk):
    def __init__(self):
        super().__init__()
        self.title("база данных учет приема пищи")
        self.geometry('1500x500')

        # раздел добавить
        self.fram_add = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.fram_add.pack(anchor='center', fill=X, padx=10, pady=10)
        self.add_title = ttk.Label(self.fram_add, text='добавить прием пищи ')
        self.add_title.pack()

        # meal
        self.meal = ttk.Label(self.fram_add, text="введите прием пищи")
        self.meal.pack()
        # окна ввода meal
        self.input_meal = ttk.Entry(self.fram_add)
        self.input_meal.pack()

        # food
        self.food = ttk.Label(self.fram_add, text="введите еду")
        self.food.pack()
        # окна ввода food
        self.input_food = ttk.Entry(self.fram_add)
        self.input_food.pack()

        # calories
        self.calories = ttk.Label(self.fram_add, text="Введите калории")
        self.calories.pack()
        # Окна ввода данных calories
        self.input_calories = ttk.Entry(self.fram_add)
        self.input_calories.pack()

        # time
        self.time = ttk.Label(self.fram_add, text="Введите время приёма пищи")
        self.time.pack()
        # Окна ввода данных time
        self.input_time = ttk.Entry(self.fram_add)
        self.input_time.pack()

        # кнопка
        self.add_button = ttk.Button(self.fram_add, text='добавить', command=self.add_mel)
        self.add_button.pack()

        # таблица
        self.fram_table = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.fram_table.pack(anchor='center', fill=X, padx=10, pady=10)
        columns = ('id', 'meal', 'food', 'calories', 'time')
        self.tree = ttk.Treeview(self.fram_table,columns=columns,show="headings")
        self.tree.pack(fill=BOTH, expand=1)
        self.table()
    def table(self):
        # очистить таблицу
        for item in self.tree.get_children():
            self.tree.delete(item)

        meals = MealsController.get()
        list_meals = []
        for meal in meals:
            list_meals.append(
                (
                    meal['id'],
                    meal['meal'],
                    meal['food'],
                    meal['calories'],
                    meal['time'],
                 )
            )

        # перевести на русский язык названия столбцов
        self.tree.heading('id',text='№')
        self.tree.heading('meal',text='прием пищи')
        self.tree.heading('food',text='еда')
        self.tree.heading('calories', text='калории')
        self.tree.heading('time', text='время')

        for meals in list_meals:
            self.tree.insert('',END,values=meals)

    # вывод
    def add_mel(self):
        MealsController.add(
            meal=self.input_meal.get(),
            food=self.input_food.get(),
            calories=self.input_calories.get(),
            time=self.input_time.get(),
        )
        self.table()
