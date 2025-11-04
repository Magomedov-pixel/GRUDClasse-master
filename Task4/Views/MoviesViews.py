from tkinter import *
from tkinter import ttk

from Task4.Controllers.MoviesControllers import MoviesController


class MoviesView(Tk):
    def __init__(self):
        super().__init__()
        self.title("учет просмотренных фильмов")
        self.geometry('1500x500')

        # раздел добавить
        self.fram_add = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.fram_add.pack(anchor='center', fill=X, padx=10, pady=10)
        self.add_title = ttk.Label(self.fram_add, text='добавить фильм')
        self.add_title.pack()

        # title
        self.title = ttk.Label(self.fram_add, text="введите название фильма")
        self.title.pack()
        # окна ввода title
        self.input_title = ttk.Entry(self.fram_add)
        self.input_title.pack()

        # year
        self.year = ttk.Label(self.fram_add, text="введите год выпуска")
        self.year.pack()
        # окна ввода phone
        self.input_year = ttk.Entry(self.fram_add)
        self.input_year.pack()

        # rating
        self.rating = ttk.Label(self.fram_add, text="Введите рейтинг фильма")
        self.rating.pack()
        # Окна ввода данных
        self.input_rating = ttk.Entry(self.fram_add)
        self.input_rating.pack()

        # кнопка
        self.add_button = ttk.Button(self.fram_add, text='добавить', command=self.add_mov)
        self.add_button.pack()

        # таблица
        self.fram_table = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.fram_table.pack(anchor='center', fill=X, padx=10, pady=10)
        columns = ('id', 'title', 'year', 'rating','watched')
        self.tree = ttk.Treeview(self.fram_table,columns=columns,show="headings")
        self.tree.pack(fill=BOTH, expand=1)
        self.table()
    def table(self):
        # очистить таблицу
        for item in self.tree.get_children():
            self.tree.delete(item)

        movies = MoviesController.get()
        list_movies = []
        for con in movies:
            list_movies.append(
                (
                    con['id'],
                    con['title'],
                    con['year'],
                    con['rating'],
                    # con['watched'],
                 )
            )

        # перевести на русский язык названия столбцов
        self.tree.heading('id',text='№')
        self.tree.heading('title',text='название')
        self.tree.heading('year',text='год выпуска')
        self.tree.heading('rating', text='рейтинг')
        self.tree.heading('watched', text='просмотренно/непросмотренно')

        for movies in list_movies:
            self.tree.insert('',END,values=movies)

    # вывод
    def add_mov(self):
        MoviesController.add(
            title=self.input_title.get(),
            year=self.input_year.get(),
            rating=self.input_rating.get(),

        )
        self.table()
