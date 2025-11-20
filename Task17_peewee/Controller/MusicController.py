from Task17_peewee.Model.Music import *

class MusicController:
    '''
    добавить трек,
    найти по исполнителю,
    треки жанра,
    альбомы года
    '''
    @classmethod
    def add(cls, title, artist, album, year, genre):
        # добавить трек
        Music.create(title=title, artist=artist, album=album, year=year, genre=genre)
    @classmethod
    def get_artist(cls, artist):
        # найти по исполнителю
        return Music.select().where(Music.artist == artist)
    @classmethod
    def get_genre(cls, genre):
        # найти по исполнителю
        return Music.select().where(Music.genre == genre)
if __name__ == '__main__':
    MusicController.add('erer','erer','erer',5,'erer')
