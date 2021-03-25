from peewee import CharField

from .base_model import BaseModel

class Publisher(BaseModel):
	name = CharField()
