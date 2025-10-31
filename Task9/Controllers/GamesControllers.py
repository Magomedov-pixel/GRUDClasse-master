from Task9.Models.Games import Games
class GamesController(Games):
    '''
     добавить игру,
     найти по жанру,
     отметить пройденной,
     игры для платформы
    '''
    obj = Games()
    @classmethod
    def get(cls):
        return cls.obj.games
    @classmethod
    def add(cls, title, genre, platform, completed):
        cls.obj.games = {"title": title, "genre": genre, "platform": platform, "completed": completed}
    #найти
    @classmethod
    def tti_genre(cls, genre):
        result = f"нет {genre}"
        for dict in cls.get():
            if dict['genre'] == genre:
                result = f"есть {genre}"
        return result
    # отметить пройденной
    @classmethod
    def completed(cls, id):
        for dict in cls.get():
            if dict['id'] == id:
                dict['completed'] = False
                return dict
        else:
            return f"фильм не пройден или {id} нет в базе"
    # для платформы
    @classmethod
    def pl_platform(cls, platform):
        result = f"нет {platform}"
        for dict in cls.get():
            if dict['platform'] == platform:
                result = f"есть {platform}"
        return result
if __name__ == '__main__':
    GamesController.add("jhfb", "rpg", "RRpsp", 'False')
    print(GamesController.get())
    GamesController.pl_platform("PC")
    print(GamesController.get())
