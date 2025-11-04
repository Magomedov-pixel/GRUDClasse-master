from tkinter import *
from tkinter import ttk

from Task9.Controllers.GamesControllers import GamesController


class GamesView(Tk):
    def __init__(self):
        super().__init__()
        self.title("база данных игр")
        self.geometry('1500x500')

        # раздел добавить
        self.fram_add = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.fram_add.pack(anchor='center', fill=X, padx=10, pady=10)
        self.add_title = ttk.Label(self.fram_add, text='добавить игру')
        self.add_title.pack()

        # title
        self.title = ttk.Label(self.fram_add, text="введите имя игры")
        self.title.pack()
        # окна ввода title
        self.input_title = ttk.Entry(self.fram_add)
        self.input_title.pack()

        # genre
        self.genre = ttk.Label(self.fram_add, text="введите жанр игры")
        self.genre.pack()
        # окна ввода genre
        self.input_genre = ttk.Entry(self.fram_add)
        self.input_genre.pack()

        # platform
        self.platform = ttk.Label(self.fram_add, text="Введите платформу")
        self.platform.pack()
        # Окна ввода данных platform
        self.input_platform = ttk.Entry(self.fram_add)
        self.input_platform.pack()

        # кнопка
        self.add_button = ttk.Button(self.fram_add, text='добавить', command=self.add_gam)
        self.add_button.pack()

        # таблица
        self.fram_table = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.fram_table.pack(anchor='center', fill=X, padx=10, pady=10)
        columns = ('id', 'title', 'genre', 'platform', 'completed')
        self.tree = ttk.Treeview(self.fram_table,columns=columns,show="headings")
        self.tree.pack(fill=BOTH, expand=1)
        self.table()
    def table(self):
        # очистить таблицу
        for item in self.tree.get_children():
            self.tree.delete(item)

        games = GamesController.get()
        list_games = []
        for game in games:
            list_games.append(
                (
                    game['id'],
                    game['title'],
                    game['genre'],
                    game['platform'],
                 )
            )

        # перевести на русский язык названия столбцов
        self.tree.heading('id',text='№')
        self.tree.heading('title',text='название игры')
        self.tree.heading('genre',text='жанр игры')
        self.tree.heading('platform', text='платформа')
        self.tree.heading('completed', text='прощел')

        for games in list_games:
            self.tree.insert('',END,values=games)

    # вывод
    def add_gam(self):
        GamesController.add(
            title=self.input_title.get(),
            genre=self.input_genre.get(),
            platform=self.input_platform.get(),
        )
        self.table()
