from peewee import *

from schema import *

models = [
    Publisher,
    Series,
    Volume,
    StoryArc,
    Playlist,
    Issue,
    Continuity,
    Universe,
]

db.create_tables(models)
