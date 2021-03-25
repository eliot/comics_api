from peewee import CharField

from .base import RefModel

class ComixologyRefSoldBy(RefModel):
	class Meta:
		db_table = 'comixology_ref_sold_by'
	seller_name = CharField(primary_key=True)
