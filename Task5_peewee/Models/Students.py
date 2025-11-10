from Task5_peewee.Models.BaseModel import *


class Students(BaseModel):

    id = PrimaryKeyField()
    name = CharField()
    age = IntegerField()
    grade = CharField()


if __name__ == '__main__':
    mysql_db.create_tables([Students])
