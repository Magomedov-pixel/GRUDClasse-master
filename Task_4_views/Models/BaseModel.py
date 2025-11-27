from Task_4_views.Connection.connection import *


class BaseModel(Model):
    class Meta:
        database = mysql_db