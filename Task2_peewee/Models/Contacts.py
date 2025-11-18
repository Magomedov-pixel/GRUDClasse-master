from Task2_peewee.Models.BasseModel import *

class Contacts(BaseModel):
    id = PrimaryKeyField()
    name = CharField()
    phone = IntegerField()
    email = CharField()


if __name__ == '__main__':
    mysql_db.create_tables([Contacts])
