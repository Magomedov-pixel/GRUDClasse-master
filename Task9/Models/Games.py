class Games:
    def __init__(self):
        self.__list_games = [
            {"id": 1, "title": "The Witcher 3", "genre": "RPG", "platform": "PC",
             "completed": True}
        ]
        self.id = 2
    @property
    def games(self):
        return self.__list_games
    @games.setter
    def games(self, dict):
        dict['id'] = self.id
        self.games.append(dict)
        self.id += 1

if __name__ == '__main__':
    gam = Games()
    print(gam.games)