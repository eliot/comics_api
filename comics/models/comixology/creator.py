from peewee import CharField, TextField

from .base import BaseModel

class ComixologyCreator(BaseModel):
	class Meta:
		db_table = 'comixology_creator'
	name = CharField() # should this be PK? or url?
	creator_id = IntegerField(primary_key=True) # ID found in Comixology creator URL e.g. https://www.comixology.com/Alan-Moore/comics-creator/2692
