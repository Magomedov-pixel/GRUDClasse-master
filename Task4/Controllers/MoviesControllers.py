from Task4.Models.Movies import Movies

class MoviesController():
    '''
    добавить фильм,
    поставить оценку,
    найти по названию,
    показать непросмотренные
    '''

    obj = Movies()
    @classmethod
    def get(cls):
        return cls.obj.movies

    #добавить фильм
    @classmethod
    def add(cls,title,year,rating):
        cls.obj.movies = {'title':title,'year':year,'rating':rating}

    #отметить просмоттреные
    @classmethod
    def watched(cls,id):
        for dict in cls.get():
            if dict['id'] == id:
                dict['watched'] = False
                return dict
        else:
            return f"фильм не просмотрен или {id} нет в базе"

    #поиск по названию.
    @classmethod
    def title_films(cls, title):
        result = f"нет {title}"
        for dict in cls.get():
            if dict['title'] == title:
                result = f"есть {title}"
        return result

if __name__ == '__main__':
    print(MoviesController.title_films('Крестный отец'))
    print(MoviesController.get())
    print(MoviesController.add('ggggg',1524,9.2))
    print(MoviesController.get())
