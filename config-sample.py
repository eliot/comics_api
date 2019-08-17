## Uncomment the database you need
#
## SQlite:
# from peewee import SqliteDatabase
# db = SqliteDatabase('my_app.db')
# 
## Postgres
from peewee import PostgresqlDatabase
db = PostgresqlDatabase('my_app', user='postgres', password='secret',
                           host='10.1.0.9', port=5432)