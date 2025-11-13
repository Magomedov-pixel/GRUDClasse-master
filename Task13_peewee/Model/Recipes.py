from Task13_peewee.Model.BaseModel import *

class Recipes(BaseModel):
    id = PrimaryKeyField()
    name = CharField()
    ingredients = CharField()
    cooking_time = IntegerField()
    difficulty = CharField()


if __name__ == '__main__':
    mysql_db.create_tables([Recipes])
