from peewee import *

mysql_db = MySQLDatabase(
    'MagoA42_equipment',
    user='MagoA42_equip',
    password='111111',
    host='10.11.13.118',
    port=3306)
if __name__ == '__main__':
    print(mysql_db.connect())
