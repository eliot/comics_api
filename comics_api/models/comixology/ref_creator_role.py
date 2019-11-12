from peewee import CharField

from .base_model import RefModel

class ComixologyRefCreatorRole(RefModel):
	'''Reference table of creative roles a person can do to an issue
	E.g. writer, inker, penciler, colorer, artist'''
	class Meta:
		db_table = 'ref_creator_role'
	role_name = CharField(primary_key=True)
