from Task9_peewee.Models.BaseModel import *


class Games(BaseModel):
    '''
    movies = [
                {
                "id": 1,
                "title": "Крестный отец",
                "year": 1972,
                "rating": 9.2,
                "watched":True
                }
]
    '''
    id = PrimaryKeyField()
    title = CharField()
    genre = CharField()
    platform = CharField()
    completed = BooleanField(default=True)

if __name__ == '__main__':
    mysql_db.create_tables([Games])