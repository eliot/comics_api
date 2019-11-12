from .base_model import ScrapeModel

class ComixologyCreator(ScrapeModel):
	class Meta:
		db_table = 'creator'
