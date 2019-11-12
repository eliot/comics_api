from peewee import CharField, DateTimeField, TextField

from .base_model import BaseModel

class Creator(BaseModel):
	'''A writer, drawer, inker, or penciler'''
	name = CharField()
	dob = DateTimeField()
	summary = TextField()
	# Nationality
	# Sex
