from Task2_peewee.Connect.connect import *

class BaseModel(Model):
    class Meta:
        database = mysql_db