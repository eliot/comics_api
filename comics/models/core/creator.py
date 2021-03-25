from peewee import CharField, DateTimeField, TextField

from .base_model import BaseModel

class Creator(BaseModel):
	'''A writer, drawer, inker, or penciler'''
	name = CharField()
	date_of_birth = DateTimeField()
	summary = TextField()
	# Nationality
	# Sex
