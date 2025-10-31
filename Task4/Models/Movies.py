class Movies:
    def __init__(self):
        self.__list_movies = [
            {
                "id": 1,
                "title": "Крестный отец",
                "year": 1972,
                "rating": 9.2,
                "watched": True}
        ]
        self.id = 2

    @property
    def movies(self):
        return self.__list_movies

    @movies.setter
    def movies(self, dict):
        dict['id'] = self.id
        self.movies.append(dict)
        self.id += 1


if __name__ == '__main__':
    mov = Movies()
    print(mov.movies)
    mov.movies = {"title": "отец","year": 2020,"rating": 9.2,}
    print(mov.movies)
