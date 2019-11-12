from peewee import CharField, TextField

from .base_model import BaseModel

class Series(BaseModel):
	# sequence of issues with the same title e.g. Detective Comics
	# e.g. Batman
	name = CharField()
	summary = TextField()
