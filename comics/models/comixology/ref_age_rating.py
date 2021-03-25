from peewee import CharField

from .base import RefModel

class ComixologyRefAgeRating(RefModel):
	class Meta:
		db_table = 'comixology_ref_age_rating'
	age_rating = CharField(primary_key=True)
