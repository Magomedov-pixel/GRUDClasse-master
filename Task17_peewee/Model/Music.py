from Task17_peewee.Model.BaseModel import *


class Music(BaseModel):
    id = PrimaryKeyField()
    title = CharField()
    artist = CharField()
    album = CharField()
    year = IntegerField()
    genre = CharField()


if __name__ == '__main__':
    mysql_db.create_tables([Music])