from peewee import CharField

from .base_model import BaseModel

class RefCreatorRole(BaseModel):
	'''Reference table of creative roles a person can do to an issue
	E.g. writer, inker, penciler, colorer, artist'''
	class Meta:
		db_table = 'ref_creator_role'
	role_name = CharField()
