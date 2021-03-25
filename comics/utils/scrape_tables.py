from comics.config import db
from comics.models.scrape import ScrapeSite, ScrapeItem, ScrapeData

def create_tables():
    models = [
        ScrapeSite,
        ScrapeItem,
        ScrapeData,
    ]

    db.create_tables(models)
