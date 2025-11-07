
from peewee import *

mysql_db = MySQLDatabase(
    database= 'MagoA42_shop',
    user = 'MagoA42_shop',
    password = '111111',
    host = '10.11.13.118',
    port = 3306
)
if __name__ == '__main__':
    print(mysql_db.connect())
