from Task19_peewee.Model.BaseModel import *


class Workouts(BaseModel):
    id = PrimaryKeyField()
    date = CharField()
    type = CharField()
    duration = IntegerField()
    calories = IntegerField()
    notes = CharField()


if __name__ == '__main__':
    mysql_db.create_tables([Workouts])