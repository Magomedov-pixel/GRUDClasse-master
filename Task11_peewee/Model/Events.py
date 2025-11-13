from Task11_peewee.Model.BaseModel import *

class Events(BaseModel):
    id = PrimaryKeyField()
    title = CharField()
    date = IntegerField()
    time = CharField()
    description = CharField()


if __name__ == '__main__':
    mysql_db.create_tables([Events])
