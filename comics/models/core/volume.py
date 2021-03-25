from peewee import CharField, IntegerField,	ForeignKeyField

from .base_model import BaseModel
# from .issue import Issue # circular import
from .series import Series

class Volume(BaseModel):
	'''
	A collection of issues in a single "book" format
	- run of the comics, e.g. volume 1 of 3 of Batman
	- has a start and end year
	'''
	name = CharField()
	number = IntegerField() # e.g. Volume 1
	issue_start_number = IntegerField()
	issue_end_number = IntegerField()
	# start_issue = ForeignKeyField(Issue, backref='volume')
	# end_issue = ForeignKeyField(Issue, backref='volume')
	series = ForeignKeyField(Series, backref='volume')
