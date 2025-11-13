from Task12_peewee.Model.BaseModel import *

class Recipes(BaseModel):
    id = PrimaryKeyField()
    name = CharField()
    status = CharField()
    deadline = IntegerField()
    priority = CharField()


if __name__ == '__main__':
    mysql_db.create_tables([Recipes])