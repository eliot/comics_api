from peewee import CharField, IntegerField

from .base import BaseModel

class ComixologyGenre(BaseModel):
	class Meta:
		db_table = 'comixology_genre'
	name = CharField()
	genre_id = IntegerField(primary_key=True)
