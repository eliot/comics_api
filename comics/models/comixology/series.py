from peewee import CharField, TextField, IntegerField

from .base import BaseModel

class ComixologySeries(BaseModel):
	class Meta:
		db_table = 'comixology_series'
	name = CharField()
	description = TextField(null=True)
	series_id = IntegerField(primary_key=True)
