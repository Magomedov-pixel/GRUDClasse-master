from Task16_peewee.Model.BaseModel import *


class Pets(BaseModel):
    id = PrimaryKeyField()
    name = CharField()
    type = CharField()
    age = IntegerField()
    owner = CharField()
    vaccinated = BooleanField(default=True)


if __name__ == '__main__':
    mysql_db.create_tables([Pets])
