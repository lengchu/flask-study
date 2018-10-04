from peewee import Model
from playhouse.pool import PooledMySQLDatabase


db = PooledMySQLDatabase ("test_py", 
                    host = '127.0.0.1', 
                    port=3306,
                    user="root",
                    passwd="root")


class BaseModel (Model):
    class Meta:
        database = db

