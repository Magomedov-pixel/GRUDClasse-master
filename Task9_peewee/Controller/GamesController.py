from Task9_peewee.Models.Games import *

class GamesComtroller:
    '''
     добавить игру,
     найти по жанру,
     отметить пройденной,
     игры для платформы
    '''
    @classmethod
    def add(cls,title,genre,platform,completed):
        # добавить игру
        Games.create(
            title = title,
            genre = genre,
            platform = platform,
            completed = completed,
        )
    @classmethod
    def get_genre(cls,genre):
        # найти по жанру
        return Games.select().where(Games.genre == genre)
    @classmethod
    def complited_F(cls):
        # отметить пройденной
        return Games.select().where(Games.completed == True)

    @classmethod
    def get_platform(cls, platform):
        # игры для платформы
        return Games.select().where(Games.platform == platform)
if __name__ == '__main__':
    GamesComtroller.add(
        "wdwd",
        "dwdw",
        "wdwdw",
        False
    )