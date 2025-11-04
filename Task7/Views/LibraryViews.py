from tkinter import *
from tkinter import ttk

from Task7.Controllers.LibraryControllers import LibraryController


class LibraryView(Tk):
    def __init__(self):
        super().__init__()
        self.title("база данных библиотеки")
        self.geometry('1500x500')

        # раздел добавить
        self.fram_add = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.fram_add.pack(anchor='center', fill=X, padx=10, pady=10)
        self.add_title = ttk.Label(self.fram_add, text='добавить книгу')
        self.add_title.pack()

        # title
        self.title = ttk.Label(self.fram_add, text="введите название")
        self.title.pack()
        # окна ввода title
        self.input_title = ttk.Entry(self.fram_add)
        self.input_title.pack()

        # author
        self.author = ttk.Label(self.fram_add, text="введите автора")
        self.author.pack()
        # окна ввода author
        self.input_author = ttk.Entry(self.fram_add)
        self.input_author.pack()

        # year
        self.year = ttk.Label(self.fram_add, text="Введите дату")
        self.year.pack()
        # Окна ввода данных year
        self.input_year = ttk.Entry(self.fram_add)
        self.input_year.pack()

        # кнопка
        self.add_button = ttk.Button(self.fram_add, text='добавить', command=self.add_lib)
        self.add_button.pack()

        # таблица
        self.fram_table = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.fram_table.pack(anchor='center', fill=X, padx=10, pady=10)
        columns = ('id', 'title', 'author', 'year', 'read')
        self.tree = ttk.Treeview(self.fram_table,columns=columns,show="headings")
        self.tree.pack(fill=BOTH, expand=1)
        self.table()
    def table(self):
        # очистить таблицу
        for item in self.tree.get_children():
            self.tree.delete(item)

        library = LibraryController.get()
        list_library = []
        for lib in library:
            list_library.append(
                (
                    lib['id'],
                    lib['title'],
                    lib['author'],
                    lib['year'],
                 )
            )

        # перевести на русский язык названия столбцов
        self.tree.heading('id',text='№')
        self.tree.heading('title',text='название')
        self.tree.heading('author',text='автор')
        self.tree.heading('year', text='дата')
        self.tree.heading('read', text='прочитанно/непрочитанно')

        for library in list_library:
            self.tree.insert('',END,values=library)

    # вывод
    def add_lib(self):
        LibraryController.add(
            title=self.input_title.get(),
            author=self.input_author.get(),
            year=self.input_year.get(),
            read=self.input_year.get(),
        )
        self.table()
