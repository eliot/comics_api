from peewee import CharField, IntegerField

from .base import BaseModel

class ComixologyPublisher(BaseModel):
	class Meta:
		db_table = 'comixology_publisher'
	name = CharField() # make PK?
	publisher_id = IntegerField(primary_key=True)
