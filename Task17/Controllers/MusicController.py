from Task17.Models.Music import Music


class MusicController:
    obj = Music()  # создать объект класса  Pet

    @classmethod
    def add(cls, title, artist, album, year, vaccinated=False):
        cls.obj.musics = {
            "title": title,
            "artist": artist,
            "album": album,
            "year": year,
            "genre": vaccinated
        }
        return True

    # прокси метод
    @classmethod
    def get(cls):
        return cls.obj.musics

    # поставить прививку,
    @classmethod
    def genre(cls, id):

        for dict in cls.get():
            if dict['id'] == id:
                dict['genre'] = True
                return dict
            else:
                return f'питомца с id {id} нет в базе данных'

    @classmethod
    def list_album(cls, album):
        list = []
        for dict in cls.get():
            if dict['album'] == album:
                list.append(dict['name'])
        return list

    # найти по типу
    @classmethod
    def type_artist(cls, artist):
        result = f"нет {artist}"
        for dict in cls.get():
            if dict['artist'] == artist:
                result = f"есть {artist}"
        return result


if __name__ == "__main__":
    print(MusicController.get())
    print(MusicController.add("Bohemian Rhapsody", "gg", "fsd", 222, "dkv"))
    print(MusicController.get())
    print(MusicController.genre(1))
    print(MusicController.list_album("A Night atthe Opera"))
    print(MusicController.type_artist("Queen"))
