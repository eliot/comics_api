from peewee import CharField, TextField, IntegerField, ForeignKeyField

from .base_model import ScrapeModel
from .series import ComixologySeries

class ComixologyVolume(ScrapeModel):
	class Meta:
		db_table = 'volume'
	
	# fields from base.Volume
	name = CharField()
	number = IntegerField() # e.g. Volume 1
	issue_start_number = IntegerField()
	issue_end_number = IntegerField()
	# start_issue = ForeignKeyField(ComixologyIssue, backref='volume')
	# end_issue = ForeignKeyField(ComixologyIssue, backref='volume')
	series = ForeignKeyField(ComixologySeries, backref='volume')
