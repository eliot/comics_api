## Uncomment the databsae you need
#
## SQlite:
# DB_URI = 'test.db'
# 
## Postgres
from peewee import PostgresqlDatabase
db = PostgresqlDatabase('my_app', user='postgres', password='secret',
                           host='10.1.0.9', port=5432)