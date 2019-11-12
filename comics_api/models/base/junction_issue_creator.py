from peewee import IntegerField, ForeignKeyField

from .issue import Issue
from .creator import Creator
from .ref_creator_role import RefCreatorRole

class IssueCreatorJunction(BaseModel):
	'''Junction table for creators and issues'''
	order = IntegerField() # ordering of artists e.g. Bob Kane (1), Joe Smith (2)
	issue = ForeignKeyField(Issue) # e.g. Batman #1
	creator = ForeignKeyField(Creator) # e.g. Bob Kane
	role = ForeignKeyField(RefCreatorRole) # e.g. "writer"
	class Meta:
		db_table = 'j_issue_creator'
		primary_key = CompositeKey('order', 'issue', 'role')
