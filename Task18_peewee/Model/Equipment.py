from Task18_peewee.Model.BaseModel import *


class Equipment(BaseModel):
    id = PrimaryKeyField()
    name = CharField()
    type = CharField()
    serial = IntegerField()
    status = CharField()
    user = CharField()


if __name__ == '__main__':
    mysql_db.create_tables([Equipment])