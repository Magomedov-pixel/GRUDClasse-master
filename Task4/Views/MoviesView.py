from Task4_peewee.Controller.MovieController import MovieController

columns = ('title','year','rating','watched')
    self.tree = ttk.Treeview(self,columns = columns,show = 'headings')
    self.trree.pack(fill=BOTH,expand =1)
def table(self):
    for item in self.thee.gett_children():
        self.tree.delete(item)
    #получить список
    films = MovieController.get()
    list_films = []
    for film in films:
        wathed = 'просмотренно'
    else:
        wathed = 'не просмотренно'
        list_films.append(
            (film.title,
            film.year,
            film.rating,
            wathed)
        )
        # заголовки таблицы
        self.tree.heading('title' text='название фильма')
        self.tree.heading('year' text='год фильма')
        self.tree.heading('reating' text='рейтинг фильма')
        self.tree.heading('wathed' text='статус фильма')

    '''
    разобратся с новым tk
    '''