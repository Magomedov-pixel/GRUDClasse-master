from Task8_peewee.Models.BaseModel import *

class Employees(BaseModel):
    id = PrimaryKeyField()
    name = CharField()
    position = CharField()
    salary = IntegerField()
    department = CharField()

if __name__ == '__main__':
    mysql_db.create_tables([Employees])