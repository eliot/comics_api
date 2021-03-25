from peewee import Model, CharField, DateTimeField, TextField
from datetime import datetime

# use a different database for each site scraped
from comics.config import db

class BaseModel(Model):
	'''A structured data item from Comixology'''
	class Meta:
		database = db
	url = CharField(null=True)
	scraped_date = DateTimeField(default=datetime.now)

class RefModel(Model):
	'''A reference table.'''
	class Meta:
		database = db
