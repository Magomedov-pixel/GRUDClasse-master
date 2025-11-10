from Task6_peewee.Models.BaseModel import *


class Expenses(BaseModel):

    id = PrimaryKeyField()
    amount = IntegerField()
    category = CharField()
    date = IntegerField()
    description = CharField()


if __name__ == '__main__':
    mysql_db.create_tables([Expenses])
