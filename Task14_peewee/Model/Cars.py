from Task14_peewee.Model.BaseModel import *


class Cars(BaseModel):
    id = PrimaryKeyField()
    brand = CharField()
    model = CharField()
    year = IntegerField()
    color = CharField()
    price = IntegerField()


if __name__ == '__main__':
    mysql_db.create_tables([Cars])
