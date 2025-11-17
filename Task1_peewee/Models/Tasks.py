from Task1_peewee.Models.BasseModel import *

class Tasks(BaseModel):
    id = PrimaryKeyField()
    task = CharField()
    completed = BooleanField(default=False)


if __name__ == '__main__':
    mysql_db.create_tables([Tasks])