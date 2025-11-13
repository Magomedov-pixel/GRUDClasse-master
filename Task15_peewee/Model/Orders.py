from Task15_peewee.Model.BaseModel import *


class Orders(BaseModel):
    id = PrimaryKeyField()
    customer = CharField()
    product = CharField()
    amount = IntegerField()
    status = CharField()
    order_date = CharField()


if __name__ == '__main__':
    mysql_db.create_tables([Orders])
