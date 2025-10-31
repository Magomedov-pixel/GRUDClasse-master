class Music:
    '''
    класс для описания каталога музыкальных треков
    методы:
        добавить трек,
        найти по исполнителю,
        треки жанра,
        альбомы года
    '''

    def __init__(self):
        self.__list_musics = [
            {"id": 1, "title": "Bohemian Rhapsody", "artist": "Queen", "album": "A Night atthe Opera", "year": 1975,
             "genre": "рок"}
        ]
        self.id = 2

    @property
    def musics(self):
        return self.__list_musics

    @musics.setter
    def musics(self, dict):
        dict['id'] = self.id
        self.musics.append(dict)


if __name__ == '__main__':
    music = Music()
    print(music.musics)
    music.musics = {"id": 1, "title": "Bohemian Rhapsody", "artist": "Queen", "album": "A Night atthe Opera",
                    "year": 1975, "genre": "рок"}
    print(music.musics)
