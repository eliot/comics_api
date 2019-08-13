from schema import *

models = [
    Publisher,
    Series,
    Volume,
    #StoryArc,
    #Playlist,
    Issue,
    ComixologyIngestedIssue,
    #Continuity,
    #Universe,
]

db.create_tables(models)
