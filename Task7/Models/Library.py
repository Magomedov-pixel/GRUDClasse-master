class Library:
    def __init__(self):
        self.__list_library = [
            {"id": 1, "title": "1984", "author": "Оруэлл", "year": 1949, "read": False}
        ]
        self.id = 2

    @property
    def library(self):
        return self.__list_library
    @library.setter
    def library(self, dict):
        dict['id'] = self.id
        self.library.append(dict)
        self.id += 1

if __name__ == '__main__':
    lib = Library()
    print(lib.library)
    lib.library = {"title": "1984", "author": "Иван", "year": 2002, "read": False}
    print(lib.library)