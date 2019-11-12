from peewee import CharField

from .base_model import RefModel

class ComixologyRefSoldBy(RefModel):
	class Meta:
		db_table = 'ref_sold_by'
	seller_name = CharField(primary_key=True)
