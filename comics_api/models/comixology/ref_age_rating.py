from peewee import CharField

from .base_model import RefModel

class ComixologyRefAgeRating(RefModel):
	class Meta:
		db_table = 'ref_age_rating'
	age_rating = CharField(primary_key=True)
