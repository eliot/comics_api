from peewee import ForeignKeyField, IntegerField, CompositeKey

from .base import RefModel
from .issue import ComixologyIssue
from .creator import ComixologyCreator
from .ref_creator_role import ComixologyRefCreatorRole

class ComixologyIssueCreatorJunction(RefModel):
	class Meta:
		db_table = 'comixology_junction_issue_creator'
		primary_key = CompositeKey('order', 'issue', 'role')
	issue = ForeignKeyField(ComixologyIssue) # e.g. Batman #1
	creator = ForeignKeyField(ComixologyCreator) # e.g. Bob Kane
	role = ForeignKeyField(ComixologyRefCreatorRole) # e.g. "wrote"
	order = IntegerField() # order of authors
