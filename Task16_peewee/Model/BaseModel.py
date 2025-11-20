from Task16_peewee.Connection.Connection import *


class BaseModel(Model):
    class Meta:
        database = mysql_db
