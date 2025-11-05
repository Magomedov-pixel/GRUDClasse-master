from tkinter import *
from tkinter import ttk

from Task13.Controllers.RecipesControllers import RecipesController


class RecipesView(Tk):
    def __init__(self):
        super().__init__()
        self.title("база данных кулинарных рецептов")
        self.geometry('1500x500')

        # раздел добавить
        self.fram_add = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.fram_add.pack(anchor='center', fill=X, padx=10, pady=10)
        self.add_title = ttk.Label(self.fram_add, text='добавить кулинарный рецепт')
        self.add_title.pack()

        # name
        self.name = ttk.Label(self.fram_add, text="введите название блюда")
        self.name.pack()
        # окна ввода name
        self.input_name = ttk.Entry(self.fram_add)
        self.input_name.pack()

        # ingredients
        self.ingredients = ttk.Label(self.fram_add, text="введите ингридиенты")
        self.ingredients.pack()
        # окна ввода ingredients
        self.input_ingredients = ttk.Entry(self.fram_add)
        self.input_ingredients.pack()

        # кнопка
        self.add_button = ttk.Button(self.fram_add, text='добавить', command=self.add_rec)
        self.add_button.pack()

        # таблица
        self.fram_table = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.fram_table.pack(anchor='center', fill=X, padx=10, pady=10)
        columns = ('id', 'name', 'ingredients')
        self.tree = ttk.Treeview(self.fram_table,columns=columns,show="headings")
        self.tree.pack(fill=BOTH, expand=1)
        self.table()
    def table(self):
        # очистить таблицу
        for item in self.tree.get_children():
            self.tree.delete(item)

        recipes = RecipesController.get()
        list_recipes = []
        for pro in recipes:
            list_recipes.append(
                (
                    pro['id'],
                    pro['name'],
                    pro['ingredients'],
                 )
            )

        # перевести на русский язык названия столбцов
        self.tree.heading('id',text='№')
        self.tree.heading('name',text='имя проекта')
        self.tree.heading('ingredients',text='ингридиенты')

        for recipes in list_recipes:
            self.tree.insert('',END,values=recipes)

    # вывод
    def add_rec(self):
        RecipesController.add(
            name=self.input_name.get(),
            ingredients=self.input_ingredients.get(),
        )
        self.table()
