from Task10_peewee.Model.BaseModel import *


class Meals(BaseModel):
    id = PrimaryKeyField()
    meal = CharField()
    food = CharField()
    calories = IntegerField()
    time = IntegerField()


if __name__ == '__main__':
    mysql_db.create_tables([Meals])
