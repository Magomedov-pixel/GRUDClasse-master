from Task7.Models.Library import Library
class LibraryController():
    '''
    добавить книгу,
    отметить прочитанной,
    найти по автору,
    книги определенного года
    '''
    obj = Library()
    @classmethod
    def get(cls):
        return cls.obj.library
    @classmethod
    def add (cls,title, author, year, read):
        cls.obj.library = {"title": title, "author": author, "year": year, "read": read}
    @classmethod
    def read(cls, id):
        for dict in cls.get():
            if dict['id'] == id:
                dict['read'] = True
                return dict
        else:
            return f'книга с id {id} прочитанна'
    @classmethod
    def author(cls,author):
        result = f"неь{author}"
        for dict in cls.get():
            if dict['author'] == author:
                result = f"есть {author}"
        return result

if __name__ == '__main__':
    print(LibraryController.get())
    print(LibraryController.add("1956","ggg",'78787','dfdf'))
    print(LibraryController.get())