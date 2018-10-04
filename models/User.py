from mysql import BaseModel
from peewee import PrimaryKeyField, CharField

class User (BaseModel):
    id = PrimaryKeyField(primary_key=True)
    username = CharField(unique = True)
    password = CharField()

