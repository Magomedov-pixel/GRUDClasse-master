from Task7_peewee.Models.BaseModel import *


class Library(BaseModel):

    id = PrimaryKeyField()
    title = CharField()
    author = CharField()
    year = IntegerField()
    read = BooleanField(default=False)

if __name__ == '__main__':
    mysql_db.create_tables([Library])
