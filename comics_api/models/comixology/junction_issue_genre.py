from peewee import ForeignKeyField

from .base_model import RefModel
from .issue import ComixologyIssue
from .genre import ComixologyGenre

class ComixologyIssueGenreJunction(RefModel):
	class Meta:
		db_table = 'j_issue_genre'
	issue = ForeignKeyField(ComixologyIssue)
	genre = ForeignKeyField(ComixologyGenre)
