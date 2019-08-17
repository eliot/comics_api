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


# Various is a special "person" on Comixology that represents multiple writers, artists, etc.
p = ComixologyPerson.create(name="Various", url='https://www.comixology.com/Various/comics-creator/1368')

