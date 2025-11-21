from Task20_peewee.Connection.Connection import *


class BaseModel(Model):
    class Meta:
        database = mysql_db
