from Task7_peewee.Models.Library import *

class LibraryController:
    '''
    добавить книгу,
    отметить прочитанной,
    найти по автору,
    книги определенного года
    '''
    @classmethod
    def add(cls,title,author,year,read):
        #добавить книгу
        Library.create(
            title=title,
            author =author,
            year = year,
            read = read
        )
    @classmethod
    def get_read_true(cls):
        #показать просмотренные
        return Library.select().where(Library.read == True)
    @classmethod
    def get_author(cls, author):
        # найти по автору
        return Library.select().where(Library.author == author)

    @classmethod
    def year(cls, year):
        # книги определенного года
        return Library.select().where(Library.year == year)
if __name__ == '__main__':
    LibraryController.add(
        "1984",
        "Оруэлл",
        1949,
        False
    )

