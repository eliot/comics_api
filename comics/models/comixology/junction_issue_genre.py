from peewee import ForeignKeyField

from .base import RefModel
from .issue import ComixologyIssue
from .genre import ComixologyGenre

class ComixologyIssueGenreJunction(RefModel):
	class Meta:
		db_table = 'comixology_junction_issue_genre'
	issue = ForeignKeyField(ComixologyIssue)
	genre = ForeignKeyField(ComixologyGenre)
