from tkinter import *
from tkinter import ttk

from Task17.Controllers.MusicController import MusicController


class MusicViews(Tk):
    def __init__(self):
        super().__init__()
        self.title("учет музыки")
        self.geometry('1500x500')

        # раздел добавить
        self.fram_add = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.fram_add.pack(anchor='center', fill=X, padx=10, pady=10)
        self.add_title = ttk.Label(self.fram_add, text='добавить музыку')
        self.add_title.pack()

        # title
        self.title = ttk.Label(self.fram_add, text="введите имя музыки")
        self.title.pack()
        # окна ввода title
        self.input_title = ttk.Entry(self.fram_add)
        self.input_title.pack()

        # genre
        self.genre = ttk.Label(self.fram_add, text="введите тип питомца")
        self.genre.pack()
        # окна ввода genre
        self.input_genre = ttk.Entry(self.fram_add)
        self.input_genre.pack()

        # year
        self.year = ttk.Label(self.fram_add, text="введите год выпуска музыки")
        self.year.pack()
        # окна ввода year
        self.input_year = ttk.Entry(self.fram_add)
        self.input_year.pack()

        # artist
        self.artist = ttk.Label(self.fram_add, text="введите имя автора")
        self.artist.pack()
        # окна ввода artist
        self.input_artist = ttk.Entry(self.fram_add)
        self.input_artist.pack()

        # кнопка
        self.add_button = ttk.Button(self.fram_add, text='добавить', command=self.add_music)
        self.add_button.pack()

        # таблица
        self.fram_table = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.fram_table.pack(anchor='center', fill=X, padx=10, pady=10)
        columns = ('id', 'title', 'artist', 'album', 'year', 'genre')
        self.tree = ttk.Treeview(self.fram_table,columns=columns,show="headings")
        self.tree.pack(fill=BOTH, expand=1)
        self.table()
    def table(self):
        # очистить таблицу
        for item in self.tree.get_children():
            self.tree.delete(item)
        # список животных
        musics = MusicController.get()
        list_musics = [] # сюда будут передоватся картежи с описанием животных
        for pet in musics:
            list_musics.append(
                (
                    pet['id'],
                    pet['title'],
                    pet['artist'],
                    pet['album'],
                    pet['year'],
                    pet['genre'],
                 )
            )

        # перевести на русский язык названия столбцов
        self.tree.heading('id',text='№')
        self.tree.heading('title',text='имя')
        self.tree.heading('artist',text='тип')
        self.tree.heading('album',text='возраст')
        self.tree.heading('year',text='имя хозяина')
        self.tree.heading('genre',text='вакцинация')
        for pet in list_musics:
            self.tree.insert('',END,values=pet)

    # вывод
    def add_music(self):
        MusicController.add(
            title=self.input_title.get(),
            genre=self.input_genre.get(),
            year=self.input_year.get(),
            artist=self.input_artist.get()
        )
        self.table()
        print(MusicController.get())
#